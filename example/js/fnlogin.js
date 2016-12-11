/**
 * Created by Aaron on 2016/12/11.
 */
function fnlogin(){
    var uname = document.getElementById("user-name");
    var pwd = document.getElementById("pwd");
    var error = document.getElementById("error_box");
    var isNotError = true;

    if (uname.value == "") {
        error.innerHTML = "用户名不能为空";
        isNotError = false;
        return;
    }else if (uname.value.charCodeAt(0) >= 48 && uname.value.charCodeAt(0) <= 57) {
        error.innerHTML = "用户名开头不能为数字";
        isNotError = false;
        return;
    }else if (uname.value.length > 20 || uname.value.length < 6 ) {
        error.innerHTML = "用户长度必须在6-20位之间";
        isNotError = false;
        return;

    }else{
        for(var i=0;i<uname.value.length;i++) {
            if ((uname.value.charCodeAt(i) > 122||uname.value.charCodeAt(i)<97) && (uname.value.charCodeAt(i)>57||uname.value.charCodeAt(i)<48)){
                error.innerHTML = "用户名只能包含小定字母和数字";
                isNotError = false;
                return;
            }
        }
    }

    if (pwd.value == ""){
        error.innerHTML = "密码不能为空";
        isNotError = false;
        return;

    }else if (pwd.value.length > 20 || pwd.value.length < 6) {
        error.innerHTML = "密码长度必须在6-20位之间";
        isNotError = false;
        return;
    }

    error.innerHTML = "登录成功";

}