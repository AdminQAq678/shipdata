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

var SignIn_btn=document.getElementById('Singin');
SignIn_btn.onclick=()=>{
    if(register_status==1){//注册状态，转为登录状态
        Name.hidden=true;
        phone.hidden=true;
        register_status=0;
    }else{
        if(UserId.value==""||Password.value==""){
            return false;
        }else{

           var data={};
           data['UserId']=UserId.value;
           data['Password']=Password.value;


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