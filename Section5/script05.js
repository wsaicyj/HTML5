/**
 * Created by Aaron on 2016/11/6.
 */
function draw(id) {
    var canvas = document.getElementById(id);
    if (canvas == null) {
        return false;
    }
    var context = canvas.getContext('2d');
    context.fillStyle = "#EEEEFF";
    context.fillRect(0,0,400,300);
    context.shadowOffsetX = 10;
    context.shadowOffsetY = 10;
    context.shadowColor = 'rgba(255,100,255,0.5)';
    context.shadowBlur = 7.5;
    //图形绘制
    context.translate(0,50);
    for (var i=0;i<3;i++){
        context.translate(50,50);
        create5Start(context);
        context.fill();
    }
}

function create5Start(context) {
    var dx = 100;
    var dy = 0;
    var s = 50;
    context.beginPath();
    context.fillStyle = 'rgba(255,0,0,0.5)';
    var dig = Math.PI / 5 * 4;
    for (var i=0;i<5;i++){
        var x = Math.sin(i * dig);
        var y = Math.cos(i * dig);
        context.lineTo(dx+x*s,dy+y*s);
    }
    context.closePath();
}