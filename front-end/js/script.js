/*Global Variables*/
var messagesRef;
var roomID;

var otherUser = "";

var thisUser = "";

function setupFirebaseHandlers() {

  messagesRef.limitToLast(10).on('child_added', function (snapshot) {
    var data = snapshot.val();
    var username = data.username;
    var images = data.text;
    var original = data.original;
    
    displayNewChat(username, images, original);
  });
}

$( document ).ready(function() {
  $(".submit-username").click(function(){
    var givenName = $(".username-textfield").text();
    if (givenName == null || givenName == "") {
      givenName = "me";
    }
    $(".username").text(givenName);
    $(".sign-up-overlay").css("display", "none");

    thisUser = givenName;
    var thisPerson = document.createElement("div");
    thisPerson.className = "person this-person";
    $(thisPerson).text(givenName);
    document.getElementById("people").appendChild(thisPerson);
    
    setupFirebaseHandlers();
  });

  roomID = $(".roomID").text() || 123456;
  messagesRef = new Firebase('https://ji-talk.firebaseio.com/'+roomID);


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

function displayNewChat(senderName, imgUrls, original) {
  var userClass = (thisUser == senderName) ? "this-user" : "other-user";

  if (userClass == "other-user" && otherUser == "") {
    otherUser = senderName;
    var otherPerson = document.createElement("div");
    otherPerson.className = "person other-person";
    $(otherPerson).text(senderName);
    document.getElementById("people").appendChild(otherPerson);
  }

  var sentence = document.createElement("div");
  sentence.className = "sentence hidden-chat " + userClass;
  for (i = 0; i < imgUrls.length; i++) {
    var emojImg =  document.createElement("img");
    emojImg.src = imgUrls[i];
    scaleImg(emojImg);
    sentence.appendChild(emojImg);
    document.getElementById("chatbox").appendChild(sentence);
          
  }

  $(sentence).attr("imgs", $(sentence).html());
  $(sentence).attr("alt", original);

  $(".hidden-chat").fadeIn(0, function(){    
      scrollToBottom();
    });

  $(sentence).hover(function(){
      $(this).html($(this).attr("alt"))

      }, function(){
      $(this).html($(this).attr("imgs"))
      })
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