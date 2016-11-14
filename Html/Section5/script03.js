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
    //图形绘制
    // context.translate(200,50);
    // context.fillStyle = 'rgba(255,0,0,0.25)';
    // for (var i = 0;i < 50;i++){
    //     context.translate(25,25);
    //     context.scale(0.95,0.95);
    //     context.rotate(Math.PI / 10);
    //     context.fillRect(0,0,100,50);
    // }
    //坐标变换与路径结合使用示例
    context.translate(200,50);
    for (var i = 0;i < 50;i++) {
        context.translate(25,25);
        context.scale(0.95,0.95);
        context.rotate(Math.PI / 10);
        create5Start(context);
        context.fill();
    }
}

function create5Start(context) {
    var dx = 100;
    var dy = 0;
    var s = 50;
    //创建路径
    context.beginPath();
    context.fillStyle = 'rgba(255,0,0,0.5)';
    var dig = Math.PI / 5 * 4;
    for(var i=0;i<5;i++){
        var x = Math.sin(i * dig);
        var y = Math.cos(i * dig);
        context.lineTo(dx + x * s,dy + y * s);
    }
    context.closePath();
}