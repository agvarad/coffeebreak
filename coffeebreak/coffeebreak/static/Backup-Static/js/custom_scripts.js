/* Custom Javascripts */


$(function() {
  $('#iconCarousel').carousel({
  interval: 5000
});

$(window).load(function(){
  $(".twentytwenty-container").twentytwenty({default_offset_pct: 0.7});  
});

$(window).load(function() {
  $('#joyRideTipContent').joyride({
     autoStart : true,
     postStepCallback : function (index, tip) {
     if (index == 2) {
       $(this).joyride('set_li', false, 1);
     }
  },
  modal:false,
  timer:5000,
  expose: true
  });
});



