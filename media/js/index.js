$('.butt').hover(over, out);
  function over(event) {
	$(this).css("cursor", "pointer");
	$(this).css("background-color","#d00");
	$(".image").fadeOut('normal');
	$("#img" + this.id).fadeIn('normal'));

  }

  function out(event) {
	$(this).css("background-color","#b00");
}


$(".linkcat").click(function() {
	var el = $(this).find("+ ul");

	if($(this).hasClass("collapsed"))

		$(el).fadeIn('normal');
	else
		$(el).fadeOut('normal');

	$(this).toggleClass("collapsed");
});
