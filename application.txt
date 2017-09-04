var url = document.getElementById("url");
var output = document.getElementById("output");
var queue = document.getElementById("queue");
var payload = document.getElementById("payload");
var host = document.getElementById("host");
var subid=document.getElementById("subs");
var unsubid=document.getElementById("unsub");
var emidas=document.getElementById("authtoken")
var client;
var subscription;

function connect() {
    client = Stomp.client(url.value);

    var headers = {
        host:host.value,
        'emidas-token':trim(emidas.value),
    }


    var connect_callback= function(){
        writeToScreen("<div id='webconn' style='font-size: 12px'>WebSocket connected</div>");

    }

    var conn_err_callback=function(error) {
        writeToScreen("ERROR: " + error);
    }

    client.connect(headers,connect_callback,conn_err_callback);

    
}


function send_message() {
    writeToScreen("Payload: " + payload.value + ", Queue: " + queue.value);
    client.send(queue.value, {}, payload.value);
}

function subscribe() {
    var headers={
       // host:'equities'
        host:host.value,
        id:subid.value
    }

    subscription = client.subscribe(queue.value, headers);
    writeToScreen(subscription+"<br>");
}


function unsubscribe() {
    var headers={
        // host:'equities'
        host:host.value,
        id:unsubid.value
    }
    client.unsubscribe(headers);

    writeToScreen("<div id='unsubed' style='font-size: 12px'>Unsubscribed: "+headers.id+"</div><br>")

}



function disconnect() {
    client.disconnect(function () {
        writeToScreen("<div id='disconnected' style='font-size: 12px'>Good Bye!!</div><br>");
    });
}

function writeToScreen(message) {
    output.innerHTML += message + "<br>";
}


function trim(str){
    return str.replace(/(^\s*)|(\s*$)/g,"");
}

function resetscreen(){
    var parentnode=document.getElementById("output");
    var children=parentnode.childNodes;
    for (i=children.length-1;i>=0;i--){
        parentnode.removeChild(children[i]);
    }
}
