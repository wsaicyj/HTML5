/**
 * Created by Aaron on 2016/11/5.
 */
function draw(id) {
    var canvas = document.getElementById(id);
    if (canvas == null) {
        return false;
    }
    var context = canvas.getContext('2d');
    //绘制渐变图形
    // var gl = context.createLinearGradient(0,0,0,300);
    // gl.addColorStop(0,'rgb(255,255,0)');
    // gl.addColorStop(1,'rgb(0,255,255)');
    // context.fillStyle = gl;
    // context.fillRect(0,0,400,300);
    // var n = 0;
    // var g2 = context.createLinearGradient(0,0,300,0);
    // g2.addColorStop(0,'rgba(0,0,255,0.5');
    // g2.addColorStop(1,'rgba(255,0,0,0.5)');
    // for (var i = 0;i < 10;i++) {
    //     context.beginPath();
    //     context.fillStyle = g2;
    //     context.arc(i * 25,i * 25,i * 10,0,Math.PI * 2,true);
    //     context.closePath();
    //     context.fill();
    // }
    //绘制径向渐变
    var g1 = context.createRadialGradient(400,0,0,400,0,400);
    g1.addColorStop(0.1,'rgb(255,255,0)');
    g1.addColorStop(0.3,'rgb(255,0,255)');
    g1.addColorStop(1,'rgb(0,255,255)');
    context.fillStyle = g1;
    context.fillRect(0,0,400,300);
    var g2 = context.createRadialGradient(250,250,0,250,250,300);
    g2.addColorStop(0.1,'rgba(255,0,0,0.5)');
    g2.addColorStop(0.7,'rgba(255,255,0,0.5)');
    g2.addColorStop(1,'rgba(0,0,255,0.5)');
    for(var i = 0;i < 10; i++){
        context.beginPath();
        context.fillStyle = g2;
        context.arc(i * 25,i * 25,i * 10,0,Math.PI * 2,true);
        context.closePath();
        context.fill();
    }

}