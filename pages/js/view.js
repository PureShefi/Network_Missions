$(document).ready(function (){
    var sponsers = [];
    sponsers = $(".sponsContainer").toArray();
    var colors = ["#F44336","#E91E63","#2196F3","#03A9F4","#00BCD4","#009688","#4CAF50","#8BC34A","#CDDC39","#FFC107","#FF9800","#FF5722","#9900FF","#CC00CC","#FF6666","#666633","#3366CC"];
    var chosen=null;
    var prev = null;
    var place = null;
    for(var i = 0;i<sponsers.length;i++)
    {
        place =Math.floor(Math.random() * colors.length);
        while(place == prev)
        {
            //if color same as before chose a different color
            place = Math.floor(Math.random() * colors.length);
        }
        chosen = colors[place];
        $(sponsers[i]).css('background-color', chosen);
        prev = place;
    }
});
$(".logo").click(function(){
    if($(this).siblings(".full").length == 0)
             $(this).siblings(".toHide").toggle();
    $(this).toggleClass("full");
});