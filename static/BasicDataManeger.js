

var myinfo_panel=$('#myinfo_panel div > input');//显示信息的输入框
for (var i =0;i<myinfo_panel.length;i++){
    myinfo_panel[i].disabled=true;
}

var add_btn=document.getElementById('add_btn');//对数据进行增加
var mod_btn=document.getElementById('mod_btn');//对数据进行修改的按钮
var query_btn=document.getElementById('query_btn');//查询按钮
var query_selection=document.getElementById('query_selection');//查询选项
var add_btn_status=0;//记录按下按钮前的状态，0为查询状态，1为编辑状态
var mod_btn_status=0;//记录按下按钮前的状态，0为查询状态，1为编辑状态
add_btn.onclick=()=>{
    //alert("hello")
    if(add_btn_status==0){//查询状态，将输入框转为可编辑状态
        for (var i =0;i<myinfo_panel.length;i++){
            myinfo_panel[i].disabled=false;
            myinfo_panel[i].value="";//增加新的资料
        }
        add_btn_status=1;
    }else if(add_btn_status==1){//编辑状态，此时可发送数据到后台
        var url='';
        var data={}
        data['length']=myinfo_panel.length;
        for(var i=0;i<myinfo_panel.length;i++){
            data['info_'+i]=myinfo_panel[i].value;//规定格式
        }
        $.post('/basicdata',data,(e)=>{
            console.log(e.data)
        })
    }

}

mod_btn.onclick=()=>{
    //alert("hello")
    if(mod_btn_status==0){//查询状态，将输入框转为可编辑状态
        for (var i =0;i<myinfo_panel.length;i++){
            myinfo_panel[i].disabled=false;//修改资料
        }
        mod_btn_status=1;
    }else if(mod_btn_status==1){//编辑状态，此时可发送数据到后台
        var url='';
        var data={};
        $.post(url,data,(e)=>{
            console.log(e.data)
        })
    }

}

query_btn.onclick=()=>{
    for (var i =0;i<myinfo_panel.length;i++){
     myinfo_panel[i].disabled=true;//禁用表单
    }

    var url='';//查询数据接口
    var data;
    $.post(url,(e)=>{
        console.log(e.data);//接收服务器返回的数据
    })
    var query_method=query_selection.selectedOptions[0].outerText;//选择的查询方式
    //查询成功或者失败都alert以下
}

