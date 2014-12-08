$(document).ready(function() {
  $(".try-it").click(function() {
    $('html, body').animate({
      scrollTop: $("#try-featurette").offset().top
    }, 600);        
  })
})

