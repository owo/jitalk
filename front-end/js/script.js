$( document ).ready(function() {
  $(".submit").click(function(){
    $(".submit").css("-webkit-animation", "circle-of-life 0.5s cubic-bezier(1,.37,.63,.82)");
    scrollToBottom();
  })

  $(".submit").bind('oanimationend animationend webkitAnimationEnd', function() { 
    $(".submit").css("-webkit-animation", "");
  });
});


function scrollToBottom() {
  $(".chatbox").scrollTop($(".chatbox")[0].scrollHeight);
}