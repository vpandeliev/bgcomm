var path = location.pathname;   
 
    var home = "/";
    $("a[href$= '" + path + "']").parents("li").each(function() { 
        $(this).addClass("current_page_item");
    });