/**
 * Created by Aaron on 2016/11/10.
 */
function saveStorage(id) {
    var data = document.getElementById(id).value;
    var time = new Date().getTime();
    localStorage.setItem(time,data);
    alert("留言成功！")
    loadStorage('msg');
}

function loadStorage(id) {
    var result = '<table border="1">';
    for (var i=0;i<localStorage.length;i++) {
        var key = localStorage.key(i);
        var value = localStorage.getItem(key);
        var date = new Date();
        date.setTime(key);
        var dateStr = date.toDateString();
        result += '<tr><td>' + value  + '</td><td>' + dateStr + '</td></tr>'
    }
    result += '</table>';
    var target = document.getElementById(id);
    target.innerHTML = result;
}

function clearStorage() {
    localStorage.clear();
    alert("数据初始化成功！");
    loadStorage('msg');
}