(function($) {
	$(document).ready(function() {
		
		$('.bs--alert-close').on('click',function(e){
			e.preventDefault();
			$(this).parent().slideUp(200);
		});		
		
	});
}(window.jQuery || window.$));