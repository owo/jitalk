/*
    This file is used for front-end requests
*/

// assuming we are using jquery

/*

SEND MESSAGES TO THE SERVER

*/

// 
$("send").ajax({

	type: 'GET', // or POST
    url: '/sendMessage',
    contentType: "application/json",
    data: {
        "roomID": $("some box").val(),
        "username": $("some box").val(),
        "text": $("some box").val()
    },
    success: function (data) {
        console.log("Message sent!")
    },
    error: function (e) {
        // not sure if that prints the error stack
        console.log("ERROR", e.message)
    }

})

/*

RECEIVE MESSAGES FROM FIREBASE
    https://www.firebase.com/tutorial/#session/gweia1nrjwu

include in <head> <script src="https://cdn.firebase.com/js/client/2.0.6/firebase.js"></script>

*/

// create a reference to firebase
var roomID = $("some value from some box") || 123456 
var messagesRef = new Firebase('https://ji-talk.firebaseio-demo.com/'+roomID);

messagesRef.limitToLast(10).on('child_added', function (snapshot) {
    //GET DATA
    var data = snapshot.val();
    var username = data.name;
    var message = data.text;
    // more data might be added 

    // you can edit the ones below on your own, however you wish

    //CREATE ELEMENTS MESSAGE & SANITIZE TEXT
    // var messageElement = $("<li>");
    // var nameElement = $("<strong class='example-chat-username'></strong>")
    // nameElement.text(username);
    // messageElement.text(message).prepend(nameElement);

    //ADD MESSAGE
    // messageList.append(messageElement)

    //SCROLL TO BOTTOM OF MESSAGE LIST
    // messageList[0].scrollTop = messageList[0].scrollHeight;
  });

