//The name of blue user
var blueUser = "";

//The name of the white user
var whiteUser = "";

$( document ).ready(function() {
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
    var inputString = getAndResetInputField();
    //ToDo: send input string to server here


    //Creating chat for testing
    blueUser = "afnan"
    whiteUser = "mahmoud"

    var selectBlueUser = Math.random()<.5; 
    var sender = selectBlueUser ? "afnan" : "mahmoud";

    var imageUrls = ["http://emojipedia.org/wp-content/uploads/2013/07/160x160x78-cat-face-with-wry-smile.png.pagespeed.ic.1ygkM3ku-M.jpg",
                     "http://emojipedia.org/wp-content/uploads/2014/04/128x128x1f63c-google-android.png.pagespeed.ic.Seerrsa2qB.png", 
                     "http://emojipedia.org/wp-content/uploads/2014/04/72x72x1f63c-twitter.png.pagespeed.ic.utvqmVWtXn.png"];
    displayNewChat(sender, imageUrls);
}

function displayNewChat(senderName, imgUrls) {
  var userClass = (whiteUser == senderName) ? "white" : "blue";

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

