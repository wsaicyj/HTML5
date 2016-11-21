/**
 * Created by Aaron on 2016/11/20.
 */
var code;
var okCount = 0;
var errCount = 0;
var charBox = document.getElementById('char');
var result = document.getElementById('result');

function show() {
    var rand = Math.random(); //获取【0，1】之间的数
    //获取一个0到26之间的一个随机数（不包含26）
    code = rand * 26;
    //获取65-90之间的任意整数
    code = Math.floor(code);
    code = code + 65;


    //将数字转换为字母
    var char = String.fromCharCode(code);

    charBox.innerHTML = char;

}

//显示字母
show();

window.onkeydown = function(ev) {

    //获取键盘值
    var key = ev.keyCode;

    if (key == code) {
        okCount++;

        charBox.className = 'animated zoomIn';
        show();

    } else {
        errCount ++;

        charBox.className = 'animated error shake';
        show();
    }
    showResult();
    setTimeout(clearAnimated,500);
}

function clearAnimated(){
    charBox.className = ''; //清除动画
}

function showResult(){
    var rate = okCount/(okCount+errCount) * 100;
    result.innerHTML = '正确:' + okCount + '个,' + '错误:' + errCount + '个，' + '正确率:' + rate.toFixed(2) + '%';
}