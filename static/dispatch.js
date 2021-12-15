// These two variables determine how many lines to add
// each time their respective box is updated.
// (See templates/home_right.html for the textarea's that they affect)
var pending_lines = 4;
var history_lines = 4;

/*
################################################################
# Our httpGet and httpGetAsync are from StackOverflow          #
# (unfortunately, my JS skills are just based on combining     #
#  snippets of other people's existing code from the internet. #
# - Matt C)                                                    #
################################################################
*/

// From: https://stackoverflow.com/a/4033310
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

// From: https://stackoverflow.com/a/4033310
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

// From: https://stackoverflow.com/a/67798771
// Slightly modified to fit needed output in doDispatch() - Matt C
async function postJsonData(jsonObject) {
    const response = await fetch("/put_dispatch", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(jsonObject)
    });
    
    const actualResponse = await response.text();
    return actualResponse;
}

// end code that's 99% StackOverflow responses

// Main funciton that's called when the user requests a new dispatch
async function doDispatch() {

    // this is also sometimes 'None', but that's dealt with by Flask
    var new_string = document.getElementById('new_request').value;

    // The only potential input to the 'decide_next_patrol' method is
    // the new_request, thank god. otherwise thise would be a nasty JSON
    // encoding.
    var data = await postJsonData({"new_request":new_string});

    // Because we're working with simple HTTP requests, I had to 
    // formalize the responsse to that endpoint. Therefore,
    // if anything at all went wrong, all we get is that ERROR... text.
    // But if it isn't an error, we get a coordinate box and a URL to a map 
    // separated by '---' (This was chosen since it's impossible for the generated
    // map URL or the coordinate box to contain that exact set of characters)
    if ( data != "ERROR---ERROR" ) {
        var parts = data.split("---");

        // Part 0 is the raw box that's been graphed. Put it in the <h3> meant for it.
        document.getElementById("dispatch_cords").innerHTML = parts[0];

        // Part 1 is the URL to the map output, so we need to set the iframe's SRC to that filename
        // but we do have to also prefix it with the endpoint name '/dispatch/maps/'
        document.getElementById("map_box").src = "/dispatch/maps/" + parts[1];

        // We also setup this <a> to allow the user to open the map in a new tab
        // also, the text gets set here so that on the initial page load the whole
        // element is hidden. :) 
        document.getElementById("maplink").href = "/dispatch/maps/" + parts[1];
        document.getElementById("maplink").innerHTML = "Open map in new tab";

        // Again, because simple HTTP, we append a '--PRED' if the result was not
        // a case, but rather an inference. If that's the case, we need to 
        // inform the user, so that the cop knows they're not going to the scene
        // of a live incident.
        if ( parts.length == 3 ) {
            // This edit is so long since it has to also retain the initial text set above (the coordinate box)
            document.getElementById("dispatch_cords").innerHTML = "<p class='alert'>This dispatch was a prediction, not a case. Use with caution.</p>" + document.getElementById('dispatch_cords').innerHTML;
        }

    } else {
        // Like we said above, we're not really able to pass a verbose error. :,(
        alert("Error.");
    }

    // This function sets off async tasks to update the two textareas on the right
    // which should show the dispatch queue, and also the past decisions we've made
    // see definition at the bottom.
    refreshLiveData();

}

// This function spawns an instance of the async GET request,
// and tells it that the response, *once* it returns, should be
// passed along to updateRefreshQueue, which does the actual
// heavylifing of updating the HTML for the user.
function initRefreshQueue() {
    httpGetAsync("/pending", updateRefreshQueue);
}

// Same as above, with the respective endpoint 
// and response handler functions defined.
function initRefreshScale() {
    httpGetAsync("/getscale", updateScaleBox);
}

// Same as above, with the respective endpoint 
// and response handler functions defined.
function initRefreshHistory() {
    httpGetAsync("/past_patrols", updateHistoryBox);
}

// This function takes the HTTP response text from the async result,
// and puts it into the correct element to make it visible to
// the end user. In this case, it's the pending calls in the
// dispatch queue.
function updateRefreshQueue(resp) {
    document.getElementById("pending_calls").innerHTML = resp;
    if ( resp != "" ) {
        pending_lines += 4;
    }
    document.getElementById('pending_calls').rows = pending_lines;
}

// Same as above, except it's updating the box containing past
// dispatch decisions, wether predictive or reactive.
function updateHistoryBox(resp) {
    document.getElementById("history_box").innerHTML = resp;
    if ( resp != "" ) {
        history_lines += 4;
    }
    document.getElementById("history_box").rows = history_lines;
}

// Same as above, except all we're doing is making sure the
// webUI and the backend are in-sync in regards to the scale
// factor applied to the response to existing calls
// (this value is ignored by predictive dispatch)
function updateScaleBox(resp) {
    document.getElementById("scale_factor").innerHTML = resp;

}

// Since the data displays on the right are independent, we've used async requests.
// Hence, this function just serves to set off the background tasks.
function refreshLiveData() {
    initRefreshQueue();
    initRefreshHistory();
    initRefreshScale();
}

// This is called by the button to set scale, hence it's ok to lock-up the UI
// while this request happens
function setScale() {
    httpGet("/setscale/" + document.getElementById('scale_factor').value);
}