/**
 * Created by Aaron on 2016/11/3.
 */
function draw(id) {
    var canvas = document.getElementById(id);
    if (canvas == null) {
        return false;
    }
    var context = canvas.getContext('2d');
    context.fillStyle = "#EEEEFF";
    context.fillRect(0,0,400,300);
    //绘画矩形
    // context.fillStyle = "red";
    // context.strokeStyle = "blue";
    // context.lineWidth = 1; 
    // context.fillRect(50,50,100,100);
    // context.strokeRect(50,50,100,100);
    //绘画圆形
    // for (var i = 0;i < 10;i++) {
    //     context.beginPath();
    //     context.arc(i * 25,i * 25,i * 10,0,Math.PI*2,true);
    //     context.closePath();
    //     context.fillStyle = 'rgba(255,0,0,0.25)';
    //     context.fill();
    // }
    //绘制复杂图形
    // context.strokeStyle = "red";
    // context.lineWidth = 2;
    // context.moveTo(0,0)
    // context.lineTo(100,200);
    // context.stroke();
    // var dx = 150;
    // var dy = 150;
    // var s = 100;
    // context.beginPath();
    // context.fillStyle = 'rgb(100,255,100)';
    // context.strokeStyle = 'rgb(0,0,100)';
    // var x = Math.sin(0);
    // var y = Math.cos(0);
    // var dig = Math.PI / 15 * 11;
    // for (var i = 0;i < 30;i++) {
    //     var x = Math.sin(i * dig);
    //     var y = Math.cos(i * dig);
    //     context.lineTo(dx + x * s,dy + y * s);
    // }
    // context.closePath() ;
    // context.fill();
    // context.stroke();
    //绘制贝济埃曲线
    var dx = 150;
    var dy = 150;
    var s = 100;
    context.beginPath();
    context.globalCompositeOperation = 'and';
    context.fillStyle =  'rgb(100,255,100)';
    var dig = Math.PI / 15 * 11;
    context.moveTo(dx,dy);
    for (var i = 0;i < 30;i++) {
        var x = Math.sin(i * dig);
        var y = Math.cos(i * dig);
        context.bezierCurveTo(dx + x * s,dy + y * s - 100,dx + x * s + 100,dy + y * s,dx + x * s,dy + y * s);
    }
    context.closePath();
    context.fill();
    context.stroke();
}