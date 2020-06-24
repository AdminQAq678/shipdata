
var query_method='query_1';
var myinfo_panel_1=$('#myinfo_panel_1 div > input');//显示信息的输入框
var myinfo_panel_2=$('#myinfo_panel_2 div > input');//显示信息的输入框
var myinfo_panel_3=$('#myinfo_panel_3 div > input');//显示信息的输入框
var myinfo_panel_4=$('#myinfo_panel_4 div > input');//显示信息的输入框


var query_btn=document.getElementById('query_btn');//查询按钮
var query_info=document.getElementById('query_info');//查询输入框

query_btn.onclick=()=>{

        myinfo_panel_1.disabled=true;
        myinfo_panel_2.disabled=true;
        myinfo_panel_3.disabled=true;
        myinfo_panel_4.disabled=true;


    var url='/querydata';
        var data={}

        data['query_method']=query_method;//查询方式
        if(query_method=='query_3'){//按照日期查询

        }else{//1 2 4都是按照名称查询
             //按船只名称查询对应的各类证书：营运证书、检验证书、安检证书、国籍配员证书的基本信息
            //查询依据
            data['query_info']=query_info.value;
        }
    $.post(url,data,(e)=>{
        // if(e.code!=200) {
        //         //     alert('查询失败，无该船的基本资料')
        //         //     return ;
        //         // }
        console.log(e.query_data_3);//接收服务器返回的数据
        //获取服务器传来的数据
        if(query_method=='query_1') {
            console.log(e.query_data_1)
            if(e.query_data_1!=null){
                for (var i = 0; i < myinfo_panel_1.length; i++) {
                    myinfo_panel_1[i].value = e.query_data_1[i]
                    myinfo_panel_1[i].disabled = true;
                }
            }
            if(e.query_data_2!=null){
                for (var i = 0; i < myinfo_panel_2.length; i++) {
                    myinfo_panel_2[i].value = e.data.query_data_2[i]
                    myinfo_panel_2[i].disabled = true;
                }
            }

            if(e.query_data_3!=null) {
                for (var i = 0; i < myinfo_panel_3.length; i++) {
                    myinfo_panel_3[i].value = e.query_data_3[i]
                    myinfo_panel_3[i].disabled = true;
                }
            }
            if(e.query_data_4!=null){
                for (var i = 0; i < myinfo_panel_4.length; i++) {
                myinfo_panel_4[i].value = e.query_data_4[i]
                myinfo_panel_4[i].disabled = true;
            }
            }

        }

        if(query_method=='query_2'){


        }
        if(query_method=='query_3'){


        }
        if(query_method=='query_4'){


        }

    })

    //查询成功或者失败都alert以下
}

var query_one=document.getElementById('query_one');
var query_two=document.getElementById('query_two');

var query_three=document.getElementById('query_three');

var query_four=document.getElementById('query_four');
query_one.onclick=()=>{
    query_method='query_1';//第一种查询方式
    document.getElementById('query_table_one').hidden=false;
    document.getElementById('query_table_two').hidden=true;

    document.getElementById('query_table_three').hidden=true;
    document.getElementById('query_table_four').hidden=true;

}

query_two.onclick=()=>{
    query_method='query_2';//第一种查询方式
    document.getElementById('query_table_one').hidden=true;
    document.getElementById('query_table_two').hidden=false;

    document.getElementById('query_table_three').hidden=true;
    document.getElementById('query_table_four').hidden=true;

}

query_three.onclick=()=>{
    query_method='query_3';//第一种查询方式
    document.getElementById('query_table_one').hidden=true;
    document.getElementById('query_table_two').hidden=true;

    document.getElementById('query_table_three').hidden=false;
    document.getElementById('query_table_four').hidden=true;

}
query_four.onclick=()=>{
    query_method='query_4';//第一种查询方式
    document.getElementById('query_table_one').hidden=true;
    document.getElementById('query_table_two').hidden=true;

    document.getElementById('query_table_three').hidden=true;
    document.getElementById('query_table_four').hidden=false;

}
