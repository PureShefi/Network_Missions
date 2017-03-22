function handleDragStart(e) {
    e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault(); // Necessary. Allows us to drop.
  }

  e.dataTransfer.dropEffect = 'move';
  return false;
}



function handleDrop(e) {
  if (e.stopPropagation) {
    e.stopPropagation(); // Stops some browsers from redirecting.
  }
    $this = $(this);
    $this.find(".leftSide").html("<div class='name'>" + e.dataTransfer.getData('text/html') + "</div>");
    return false;
}

var cols = document.querySelectorAll('.drag');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragstart', handleDragStart, false);
});

var cols = document.querySelectorAll('.dropBox');
[].forEach.call(cols, function(col) {
  col.addEventListener('dragover', handleDragOver, false);
  col.addEventListener('drop', handleDrop, false);
});

$(".leftSide").dblclick(function () {
    $(this).html("");
});

$(".glyphicon-plus").click( function(e) {
    $this = $(this).prev().prev();
    time = $this.html().split(":"); 
    if(time[1]=="00")
        time[1] = "30";
    else{
        time[1] = "00";
        time[0] = parseInt(time[0])+1;
    }
    if(time[0] == "24")
        time[0] = "0";
    $this.html(time[0]+":" + time[1]);
});
$(".glyphicon-minus").click( function(e) {
    $this = $(this).prev();
    time = $this.html().split(":");
    if(time[0] == "0" && time[1] == "00")
        time[0] = "24";
    if(time[1]=="30")
        time[1] = "00";
    else{
        time[1] = "30";
        time[0] = parseInt(time[0])-1;
    }
    $this.html(time[0]+":" + time[1]);
});