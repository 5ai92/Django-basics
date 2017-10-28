$(document).ready(function(){
	if ($(window).width() < 1024){
		$container = $('.container-fluid');
		$content = $('.content');
		$container.removeClass('container-fluid');
		$content.addClass('container-fluid');
		var screenWidth = $(window).width();
		//$('#homepage-slider').css('width': screenWidth);
	}
});

$('.carousel-play-btn').click(function(){
	$('#videoModal').modal('show');
});

$('#btn1').click(function(){
	event.preventDefault();
  $('.full-movies-slider').animate({
    scrollLeft: "-=200px"
  }, "slow");
});

$('#btn2').click(function(){
	$('.full-movies-slider').animate({
    scrollLeft: "+=200px"
  }, "slow");
});