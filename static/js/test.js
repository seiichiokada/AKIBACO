$(function(){
	$('.gazo').click(function(){
		if($(this).hasClass('open') == false){
			$(this).attr('src', 'static/img/Chairred.png').addClass('open');
		}else{
			$(this).attr('src', 'static/img/chairgreen.png').removeClass('open');
		}
	});
});