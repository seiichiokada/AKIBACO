$(function(){
	$('.gazo').click(function(){
		var seat_id = $(this).attr ("id");
		console.log(seat_id);
		



		if($(this).hasClass('open') == false){
			$(this).attr('src', 'static/img/Chairred.png').addClass('open');




			
			// const sqlite3 = require('sqlite3').verbose();
    		// const db = new sqlite3.Database("../../akibacoDB.db");

			// db.run("updete map set use_seat = 1 where id = seat_id");
			
			
			// db.close();			

		}else{
			$(this).attr('src', 'static/img/chairgreen.png').removeClass('open');
		







		}
	});
});