

var myinfo_panel=$('#myinfo_panel div > input');//显示信息的输入框
for (var i =0;i<myinfo_panel.length;i++){
    myinfo_panel[i].disabled=true;
}

var add_btn=document.getElementById('add_btn');//对数据进行增加
var mod_btn=document.getElementById('mod_btn');//对数据进行修改的按钮
var query_btn=document.getElementById('query_btn');//查询按钮
var del_btn=document.getElementById('del_btn');//删除按钮
var add_btn_status=0;//记录按下按钮前的状态，0为查询状态，1为编辑状态
var mod_btn_status=0;//记录按下按钮前的状态，0为查询状态，1为编辑状态
var query_selection=document.getElementById('query_selection');//查询选项
var query_info=document.getElementById('query_info');//查询输入框
var del_info=document.getElementById('del_info');//删除输入框


add_btn.onclick=()=>{
    //alert("hello")
    mod_btn_status=0;
    if(add_btn_status==0){//查询状态，将输入框转为可编辑状态
        myinfo_panel[0].value="";
        for (var i =1;i<myinfo_panel.length;i++){
            myinfo_panel[i].disabled=false;
            myinfo_panel[0].value="";//增加新的资料
        }

        add_btn_status=1;
    }else if(add_btn_status==1){//编辑状态，此时可发送数据到后台
        var url='';
        var data={}
        data['length']=myinfo_panel.length;
        for(var i=1;i<myinfo_panel.length;i++){
            data['info_'+i]=myinfo_panel[i].value;//规定格式
        }
        data['operation']='add';
        $.post('/basicdata',data,(e)=>{
            console.log(e.data)
        })
    }

}

mod_btn.onclick=()=>{
    //alert("hello")
    add_btn_status=0;
    if(mod_btn_status==0){//查询状态，将输入框转为可编辑状态

        for (var i =1;i<myinfo_panel.length;i++){
            myinfo_panel[i].disabled=false;//修改资料
        }
        myinfo_panel[0].disabled=true;
        // myinfo_panel[1].disabled=true;
        mod_btn_status=1;
    }else if(mod_btn_status==1){//编辑状态，此时可发送数据到后台

        var url='/basicdata';
        var data={}
        data['length']=myinfo_panel.length;
        for(var i=0;i<myinfo_panel.length;i++){
            data['info_'+i]=myinfo_panel[i].value;//规定格式
        }
        data['operation']='mod';
        $.post(url,data,(e)=>{
            console.log(e.data)
        })
    }

}

query_btn.onclick=()=>{
    for (var i =0;i<myinfo_panel.length;i++){
     myinfo_panel[i].disabled=true;//禁用表单
    }

    var url='/basicdata';
        var data={}
        data['length']=myinfo_panel.length;
        for(var i=0;i<myinfo_panel.length;i++){
            data['info_'+i]=myinfo_panel[i].value;//规定格式
        }
        data['operation']='query';
        var query_method=query_selection.selectedOptions[0].outerText;//选择的查询方式
        data['query_method']=query_method;
        data['query_info']=query_info.value;
    $.post(url,data,(e)=>{
        if(e.code!=200) {
            alert('查询失败，无该船的基本资料')
            return ;
        }
        console.log(e.data);//接收服务器返回的数据
        for (var i =0;i<myinfo_panel.length;i++){
            myinfo_panel[i].value=e.data[i]
            myinfo_panel[i].disabled=true;
        }

    })

    //查询成功或者失败都alert以下
}


del_btn.onclick=()=>{
    // for (var i =0;i<myinfo_panel.length;i++){
    //  myinfo_panel[i].disabled=true;//禁用表单
    // }

    var url='/basicdata';
        var data={}
        data['operation']='del';
        data['del_info']=del_info.value;//根据船名删除基本资料
    $.post(url,data,(e)=>{
        if(e.code!=200) {
            alert('删除失败，不存在该船的基本资料');
            return ;
        }else{
             alert('删除资料成功')
        }
        console.log(e.data);//接收服务器返回的数据


    })

    //查询成功或者失败都alert以下
}
