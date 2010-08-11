$('.linkcat').addClass("collapsed");
  $('.linkcat').hover(over, out);
  function over(event) {
$(this).css("cursor", "pointer");
  }

  function out(event) {

}

$(".linkcat").click(function() {
	var el = $(this).find("+ ul");

	if($(this).hasClass("collapsed"))

		$(el).fadeIn('normal');
	else
		$(el).fadeOut('normal');

	$(this).toggleClass("collapsed");
});
