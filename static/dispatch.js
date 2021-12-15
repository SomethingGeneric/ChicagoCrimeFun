// funny js go brr

var pending_lines = 4;
var history_lines = 4;

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

function doDispatch() {

    var new_string = document.getElementById('new_request').value.replaceAll(",","CS"); // look man form data is a lot of work :,(

    var data = httpGet("/do_dispatch/" + new_string);

    if ( data != "ERROR---ERROR" ) {
        var parts = data.split("---");
        document.getElementById("dispatch_cords").innerHTML = parts[0];
        document.getElementById("map_box").src = "/dispatch/maps/" + parts[1];

        if ( parts.length == 3 ) {
            document.getElementById("dispatch_cords").innerHTML = "<div class='alert'>This dispatch was a prediction, not a case. Use with caution.</div><br/>" + document.getElementById('dispatch_cords').innerHTML;
        }

    } else {
        alert("Been borked.");
    }

    refreshLiveData();

}

function initRefreshQueue() {
    httpGetAsync("/pending", updateRefreshQueue);
}

function updateRefreshQueue(resp) {
    document.getElementById("pending_calls").innerHTML = resp;
    if ( resp != "" ) {
        pending_lines += 4;
    }
    document.getElementById('pending_calls').rows = pending_lines;
}

function initRefreshHistory() {
    httpGetAsync("/past_patrols", updateHistoryBox);
}

function updateHistoryBox(resp) {
    document.getElementById("history_box").innerHTML = resp;
    if ( resp != "" ) {
        history_lines += 4;
    }
    document.getElementById("history_box").rows = history_lines;
}

function refreshLiveData() {
    initRefreshQueue();
    initRefreshHistory();
}