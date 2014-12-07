/*Global Variables*/
var messagesRef;
var roomID;

var otherUser = "";

var thisUser = "";

function setupFirebaseHandlers() {

  messagesRef.limitToLast(10).on('child_added', function (snapshot) {
    var data = snapshot.val();
    var username = data.name;
    var images = data.text;

    displayNewChat(username, images);
  });
}

$( document ).ready(function() {
  roomID = $(".roomID").text() || 123456 
  messagesRef = new Firebase('https://ji-talk.firebaseio.com/'+roomID);

  setupFirebaseHandlers();

  thisUser = $(".username").text();

  $(document).keypress(function(event) {
    if (event.keyCode == 13) {
        event.preventDefault();
        sendChatMsg();
    }
  });

  $(".submit").click(function(){
    sendChatMsg();
  })

  $(".submit").bind('oanimationend animationend webkitAnimationEnd', function() { 
    $(".submit").css("-webkit-animation", "");
  });
});

function sendChatMsg() {
  $(".submit").css("-webkit-animation", "circle-of-life 0.5s ease-in");
  sendToServer(getAndResetInputField());

  // generateDummyData();
}

function displayNewChat(senderName, imgUrls) {
  var userClass = (thisUser == senderName) ? "this-user" : "other-user";

  var sentence = document.createElement("div");
  sentence.className = "sentence hidden-chat " + userClass;
  for (i = 0; i < imgUrls.length; i++) {
    var emojImg =  document.createElement("img");
    emojImg.src = imgUrls[i];
    scaleImg(emojImg);
    sentence.appendChild(emojImg);
    document.getElementById("chatbox").appendChild(sentence);
          
    $(".hidden-chat").fadeIn(0, function(){
      //$(this).css("-webkit-animation", "circle-of-life 0.5s ease-in");
      //$(this).removeClass(".hidden-chat");
      scrollToBottom();
    });
  }
}

function sendToServer(string) {
  $.ajax({
    type: 'GET', // or POST
      url: '/sendMessage',
      contentType: "application/json",
      dataType: "json",
      data: { 
          "roomID": roomID,
          "username": thisUser,
          "text": string
      },
      success: function (data) {
          console.log("Message sent!")
      },
      error: function (e) {
          console.log("ERROR", e.message)
      }
  })
}

function getAndResetInputField() {
  var input = $(".input-field").text();
  $(".input-field").text("");
  return input;
}

function scrollToBottom() {
  $('.chatbox').scrollTop($(".chatbox")[0].scrollHeight);
}

function scaleImg(img){
  img.style.height = "50px";
}

function generateDummyData() {
  //Creating chat for testing
  otherUser = "afahim"
  thisUser = "mahmoud"

  var selectOtherUser = Math.random()<.5; 
  var sender = selectOtherUser ? "afahim" : "mahmoud";

  var imageUrls = ["http://emojipedia.org/wp-content/uploads/2013/07/160x160x78-cat-face-with-wry-smile.png.pagespeed.ic.1ygkM3ku-M.jpg",
                   "http://emojipedia.org/wp-content/uploads/2014/04/128x128x1f63c-google-android.png.pagespeed.ic.Seerrsa2qB.png", 
                   "http://emojipedia.org/wp-content/uploads/2014/04/72x72x1f63c-twitter.png.pagespeed.ic.utvqmVWtXn.png"];

  displayNewChat(sender, imageUrls);
}

