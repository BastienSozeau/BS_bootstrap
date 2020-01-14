(function($) {
	$(document).ready(function() {
		
// Alert
		$('.bs--alert-close').on('click',function(e){
			e.preventDefault();
			$(this).parent().slideUp(200);
		});		

// Menu
		$('.bs--menu-item').on('click',function(){
			$(this).parent().children('.bs--menu-item').removeClass('active');
			$(this).addClass('active');
		});		
		
	});
}(window.jQuery || window.$));