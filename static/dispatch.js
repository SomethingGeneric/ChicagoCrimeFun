// funny js go brr

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
    } else {
        alert("Been borked.");
    }

}

function initRefreshQueue() {
    httpGetAsync("/pending", updateRefreshQueue);
}

function updateRefreshQueue(resp) {
    document.getElementById("pending_calls").innerHTML = resp;
}