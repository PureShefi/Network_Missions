$(document).scroll(function () {
     $("li").removeClass("active");
    if($(document).scrollTop()+50<$(window).height())
    {
        $("nav").removeClass("navbar-default");
        $("nav").addClass("before");
    }
    else
    {
        $("nav").removeClass("before");
        $("nav").addClass("navbar-default",200, "easeInCubic" ); 
    }

    $(".info").css({opacity:1-$(document).scrollTop()/($(window).height()/2)});
    changeActive();
});

function changeActive(){
    if($(document).scrollTop()>$(window).height()-1 && $(document).scrollTop()/2<$(window).height())
    {
        $("#sec2").addClass("active");
    }
    if($(document).scrollTop()/2>$(window).height()-1 && $(document).scrollTop()/3<$(window).height())
    {
        $("#sec3").addClass("active");
    }
}