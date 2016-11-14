/**
 * Created by Aaron on 2016/11/6.
 */
// function draw(id) {
//     var canvas = document.getElementById(id);
//     if (canvas == null) {
//         return false;
//     }
//     var context = canvas.getContext('2d');
//     context.fillStyle = "#EEEEFF";
//     // context.fillRect(0,0,400,300);
//     var image = new Image();
//     image.src = "../img/4.jpg"
//     image.onload = function() {
//         // drawImg(canvas,context,image);
//         //创建填充样式，全方向平铺
//         var ptrn = context.createPattern(image,'repeat');
//         //指定填充样式
//         context.fillStyle = ptrn;
//         //填充画布
//         context.fillRect(0,0,400,300);
//     }
// }


// function drawImg(canvas,context,image) {
//     // for (var i=0;i<7;i++) {
//     //     context.drawImage(image,0 + i*50,0 + i*25,100,100);
//     // }
//     // context.drawImage(image,0,0,100,100);
//     // //绘制将局部区域进行放大后的图像
//     // context.drawImage(image,23,5,57,80,110,0,100,100);
//     //图像平铺
//     var scale = 2;
//     var n1 = image.width/scale;
//     var n2 = image.height/scale;
//     var n3 = canvas.width/n1;
//     var n4 = canvas.height/n2;
//     for (var i=0;i<n3;i++){
//         for(var j=0;j<n4;j++){
//             context.drawImage(image,i*n1,j*n2,n1,n2);
//         }
//     }
// }



function draw(id) {
    var canvas = document.getElementById(id);
    if (canvas == null){
        return false;
    }
    var context = canvas.getContext('2d');
    var gr = context.createLinearGradient(0,400,300,0);
    gr.addColorStop(0,'rgb(255,255,0)');
    gr.addColorStop(1,'rgb(0,255,255)');
    context.fillStyle = gr;
    context.fillRect(0,0,400,300);
    var image = new Image();
    image.src = "../img/4.jpg";
    image.onload = function() {
        drawImg(context,image);
    }
}

function drawImg(context,image) {
    create5StarClip(context);
    context.drawImage(image,-50,-150,300,300);
}

function create5StarClip(context){
    var dx = 100;
    var dy = 0;
    var s = 150;
    context.beginPath();
    context.translate(100,150);
    var dig = Math.PI / 5 * 4;
    for (var i=0;i<5;i++) {
        var x = Math.sin(i * dig);
        var y = Math.cos(i * dig);
        context.lineTo(dx+x*s,dy+y*s);
    }
    context.clip();
}