var Register=document.getElementById('Register');
var UserId=document.getElementById('UserId');
var Password=document.getElementById('Password');

var Name=document.getElementById('Name');//员工姓名
var phone=document.getElementById('phone');//员工电话
var register_status=0;//0为登录状态，1为注册状态
var phoneNumber=document.getElementById('phoneNumber');
var UserName=document.getElementById('UserName');
var theform=document.getElementById('theform');
Register.onclick=()=>{//登录
    if(register_status==0){
        Name.hidden=false;
        phone.hidden=false;
        register_status=1;
        return ;
    }
    var s={}
    if (valid_code_info.value.toString().toLowerCase()!=String(valid_code_code.innerText).toLowerCase() ){
             console.log(valid_code_info.value.toString().toLowerCase())
            console.log(String(valid_code_code.innerText).toLowerCase())
            alert('验证码输入错误，请重新输入');
        }
    else 
    if(UserId.value!=""&&Password.value!=""){
        s['UserId']=UserId.value;
        s['Password']=Password.value;
        s['UserName']=UserName.value;
        s['phoneNumber']=phoneNumber.value;
        console.log(phoneNumber.value)
        $.post('/register',s,(e)=>{
        alert(e.data)
        console.log(e)
        if(e.data=="register sucess"){
            console.log("register sucess")
        }
        Name.hidden=true;
        phone.hidden=true;
        register_status=0;
    })
    }
}

//theform.onsubmit=()=>{
//    if(UserId.value==""||Password.value==""||UserName.value==""||phoneNumber.value=="") return false;
//}
var valid_code_info=document.getElementById('valid_code_info');//验证码输入框
var valid_code_img=document.getElementById('valid_code_img');//验证码图片
var valid_code_code=document.getElementById('valid_code_code');//验证码
var SignIn_btn=document.getElementById('Singin');
SignIn_btn.onclick=()=>{
    if(register_status==1){//注册状态，转为登录状态
        Name.hidden=true;
        phone.hidden=true;
        register_status=0;
    }else{
        if(UserId.value==""){
            alert('用户ID不可为空，请重新输入');
            return false;
        }else if (Password.value=="" ){
            alert('用户密码不可为空，请重新输入');

        }else if (valid_code_info.value.toString().toLowerCase()!=String(valid_code_code.innerText).toLowerCase() ){
             console.log(valid_code_info.value.toString().toLowerCase())
            console.log(String(valid_code_code.innerText).toLowerCase())
            alert('验证码输入错误，请重新输入');
        }

        else{

           var data={};
           data['UserId']=UserId.value;
           data['Password']=Password.value;
           //data['valid_code']=valid_code_code.innerText;

           $.ajax({
           type: "post",
           url: "/login",
           data: data,
       }).success(function(e) {
         console.log(e.data)
            if(e.data=='登录成功'){
            alert(e.data)
                window.location="/";//登录成功跳转到首页
            }else{
                alert(e.data)
            }
       }).fail(function(err){
         console.log(err)
       })

        }

    }


}

$('#theform').on('submit', function(){
//      registPost()
     event.preventDefault() //阻止form表单默认提交
})

valid_code_img.onclick=()=>{

    $.get('/getValid_code',(e)=>{

        if(e.data=='获取验证码成功'){
            valid_code_img.src+='?'//刷新图片资源
            valid_code_code.innerText=e.code;
            console.log(valid_code_code)
        }
    });
}