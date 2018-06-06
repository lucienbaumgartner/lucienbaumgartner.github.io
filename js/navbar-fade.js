var $nav = $("#navigation");
if(scrolltop >= $nav.offset().top + $nav.height()) {
  $('#fixedbar').fadeIn(250);
}
else {
  $('#fixedbar').fadeOut(250);
}
