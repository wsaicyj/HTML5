 /**
 * Created by Aaron on 2016/11/6.
 */
function draw(id) {
     var canvas = document.getElementById(id);
     if (canvas == null) {
         return false;
     }
     var context = canvas.getContext('2d');
     var oprtns = new Array (
         "source-atop",
         "source-in",
         "source-out",
         "source-over",
         "destination-atop",
         "destination-in",
         "destination-out",
         "destination-over",
         "lighter",
         "copy",
         "xor"
     );
     var i = 8; //读者可自行修改该参数来显示想要查看的组合效果
     //绘制原有图形（蓝色长方形）
     context.fillStyle = "blue";
     context.fillRect(10,10,60,60);
     context.globalCompositeOperation = oprtns[i];
     //设置红色圆形
     context.beginPath();
     context.fillStyle = "red";
     context.arc(60,60,30,0,Math.PI*2,false);
     context.fill();
 }