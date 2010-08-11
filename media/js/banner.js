


	var currentTime = new Date();
	var next = currentTime.getSeconds()%6;
	var str1 = "";
	filename = str1.concat("banners/banner").concat(next).concat(".jpg");
	property = str1.concat("url(media/banners/banner").concat(next).concat(".jpg)");
	//alert(property);
	$("#header").css("background-image", property);


