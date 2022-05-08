$(function () {
    $('#exampleInputName').blur(function () {
        var name = $(this).val();
        var reg = /^[a-z]{3,6}$/;
        b = reg.test(name);
        if(b){
            // $('#nameinfo').html('可以').css({'color': 'green', 'font-size': 16});
            $.getJSON(
                '/axfuser/checkname/',
                {'name':name},
            function (data) {
                if(data['status'] === 200){
                    $('#nameinfo').html(data['msg']).css({'color':'green','font-size':16});
                }else{
                    $('#nameinfo').html(data['msg']).css({'color':'red','font-size':16});
                }
            }
            )
        }
        else {
            $('#nameinfo').html('用户名格式不正确').css({'color':'red','font-size':16});
        }
    })
});

//===================================================================================================

$(function () {
    $('#exampleInputPassword1').blur(function () {
        var pwd66 = $(this).val();
        if(pwd66){
        }else {
            $('#pwd66').html('密码不能为空').css({'color':'red','font-size':16})
        }
    })
});

$(function () {
    $('#exampleInputPassword2').blur(function () {
        var pwd1 = $('#exampleInputPassword1').val();
        var pwd2 = $(this).val();
        if(pwd1 === pwd2 ){
            $('#pwdinfo').html('密码一致').css({'color':'green','font-size':16})
        }else{
            $('#pwdinfo').html('密码一致').css({'color':'green','font-size':16})
        }
    })
});













//
// //    密码一致性校验
//     $('#passwordconfirm').blur(function () {
//         var password = $('#password').val();
//         var passwordconfim = $(this).val();
//
//         if(password == passwordconfim){
//
//         }else{
//             $('#passwordinfo').html('❌密码不一致').css({'color':'red','font-size':10});
//         }
//
//     })
//
//
// })
//
//
// function parse1(){
//     var password = document.getElementById('password').value;
//     password = md5(password)
//
//     document.getElementById('password').value = password
//
//
//     return true
// }
