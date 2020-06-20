var query_btn=document.getElementById("query");
var add_btn=document.getElementById("add");
var real_add_btn=document.getElementById("add_btn");
var del_btn=document.getElementById("del");
var mod_btn=document.getElementById("modify");
var sql="";
var api="/navigationFee"
var delOrMod_btn;//表格右边删除按钮
var aj=new XMLHttpRequest();
var td=document.getElementsByTagName("td");//表单元格
var tr=document.getElementsByTagName("tr");//表行
var th=document.getElementsByTagName("th");//表头
var realtable=document.getElementById("realtable");//表格
// var tableVersion=$("#tableVersion").children()[0].innerText;

var isEdittabShowing= false;
var chgFlag=false;
var chgdbandtabbtn=document.getElementById('chgdbandtabbtn');
var myinfo_panel=$('#myinfo_panel div > input');
var tabSelection=document.getElementById('tab_selection');//选择表
var tableVersion=$(tabSelection).children()[tabSelection.selectedIndex].value;
var submit_btn=document.getElementById('submit_btn');//提交按钮
var status=0;//当前状态 0为查询状态 ，1为增加...
/*  切换表    */
tabSelection.onchange=()=>{
    //当前表名
    var value=$(tabSelection).children()[tabSelection.selectedIndex].value;
    console.log(value)
    tableVersion=value;
    if(status!=1)
    query_btn.click();
}
/*     */
for (var i=2;i<tr.length;i++){
	tr[i].innerHTML+="<button class='delOrMod_btn'hidden></button>"
}
//删除/修改按钮
delOrMod_btn=document.getElementsByClassName('delOrMod_btn');
// console.log(delOrMod_btn)
/*      查询请求    */
function queryfunc(){
    var data={};                                //传入到后端的参数
    //根据表名去查询
    data['operation']='query'                   //操作为查询
    data['tableVersion']=tableVersion;          //表名
    // console.log('表名',tableVersion)
    data['method']='all';                       //查询所有数据
	$.post(api,data,(e)=>{
	    console.log("查询成功")
        console.log(e.data)
        console.log('ok')
           var head=e.head;                     //表头数据
           var data1=e.data;                    //表体
           //console.log(head);
           //console.log(data1);
           var trLength=tr.length;
           for (var i =1;i<trLength;i++)        //删除原表数据
           {
               // console.log(i)
               realtable.deleteRow(1);

           }

           var t=realtable.insertRow(tr.length);
           //插入表头
           for (var i=0;i<head.length;i++){
               var tem=t.insertCell(i);
               tem.innerText=head[i][0]
           }
           // 插入表体
           for (var i=0;i<data1.length;i++){
                 var t=realtable.insertRow(tr.length);
                 for (var k=0;k<data1[i].length;k++){
                   var tem=t.insertCell(k);
                   tem.innerText=data1[i][k]
                   }
           }
           //添加修改/删除按钮
            for (var i=2;i<tr.length;i++){
	    tr[i].innerHTML+="<button class='delOrMod_btn' hidden></button>"
    }
    //给修改/删除按钮添加监听
	AddListener();
	})
}

//顶部查询选项按钮
query_btn.onclick=()=>{
    status=0;                                       //查询状态，此状态切换表会触发查询
    realtable.hidden=false;
    $('#query_table_one').children()[0].hidden=true;//显示数据表格隐藏
    $('#query_table_one').children()[1].hidden=false;//添加数据面板显示
	for (var i=0;i<delOrMod_btn.length;i++){
	delOrMod_btn[i].hidden=true;
	}
	
	submit_btn.hidden=true;                 //隐藏提交按钮
    queryfunc();                            //查询请求
    addEditlistener();                      //给表格添加可编辑逻辑
	chgFlag=false;
}
//顶部增加选项按钮
add_btn.onclick=()=>{//添加用户按钮
    status=1;
     $('#query_table_one').children()[0].hidden=false;
    $('#query_table_one').children()[1].hidden=true;
    realtable.hidden=true;
	for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=true;
	}


    chgFlag=false;
	
}
//顶部删除选项按钮
del_btn.onclick=()=>{
    status=2;
    realtable.hidden=false;
    $('#query_table_one').children()[0].hidden=true;
    $('#query_table_one').children()[1].hidden=true;
    option="del"

	for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=false;
		delOrMod_btn[i].innerText="删除"
	}
	submit_btn.hidden=true;
	 if(isEdittabShowing) {
	     if(tr.length!=0)//数据不为空的情况
        tr[tr.length-1].hidden=true;
        isEdittabShowing=false;
    }
    chgFlag=false;

}
//顶部修改选项按钮
mod_btn.onclick=()=>{
    status=3;
     realtable.hidden=false;
     $('#query_table_one').children()[0].hidden=true;
    $('#query_table_one').children()[1].hidden=true;
    //tableVersion=""

    //查询要修改的表的数据
    var data={};
    data['tableVersion']=tableVersion;
    data['method']='all'
	$.post(api,data,(e)=>{
	    console.log("查询成功")
        console.log(e.data)
        console.log('ok')
           // var head=e.head;
           var data1=e.data;
           // console.log(head);
           console.log(data1);
           var trLength=tr.length;
           for (var i =2;i<trLength;i++)
           {
               console.log(i)
               realtable.deleteRow(2);

           }

           // var t=realtable.insertRow(tr.length);
           // //插入表头
           // for (var i=0;i<head.length;i++){
           //     var tem=t.insertCell(i);
           //     tem.innerText=head[i][0]
           // }
           //插入表体
           for (var i=0;i<data1.length;i++){
                 var t=realtable.insertRow(tr.length);
                 for (var k=0;k<data1[i].length;k++){
                   var tem=t.insertCell(k);
                   tem.innerText=data1[i][k]
                   }
           }
            for (var i=2;i<tr.length;i++){
	    tr[i].innerHTML+="<button class='delOrMod_btn' ></button>"
    }

    for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=false;
		delOrMod_btn[i].innerText="修改"
	}
    AddListener();
    addEditlistener()
	})

    option="chgdata"

	submit_btn.hidden=true;
	   if(isEdittabShowing) {
        tr[tr.length-1].hidden=true;
        isEdittabShowing=false;
    }
    chgFlag=true;

}

var option="chgdata"
//给删除修改按钮添加监听
function AddListener(){

    for(var i=0;i< delOrMod_btn.length;i++){
        delOrMod_btn[i].onclick=function modify_opration(e){//设置修改删除按钮的监听
        var theClickedBtn=e.srcElement;


         var children=$(e.srcElement).parent().children()
        var s={}
        //var prevalue=[];
        s['tableVersion']=tableVersion
            var len=$($(tr)[1]).children().length;
        for(var k=0;k<len;k++){
          //使用encodeURIComponentd对传入服务器的参数名进行url编码
          //防止出现服务器无法获取到中文参数的问题
          s[encodeURIComponent($($(tr)[1]).children()[k].innerText)]=children[k].innerText;
          console.log('参数',children[k].innerText)

        }

        console.log(s)
            s['operation']='del'
            if(option=='chgdata'){
                s['operation']='update'
            }

           $.post(api,s,(e)=>{//根据option的不同去修改或者删除
                r=e;
                console.log(e.data)
                if(e.data=="删除成功"){
                    alert('删除成功');
                    var index=$(theClickedBtn).parent().index();//被删除行所在索引
                    $(realtable)[0].deleteRow(index);
                }
                if(e.data=="修改成功"){
                    alert(e.data)
                }
                // $(e.srcElement).parent()[0].contentEditable=false;//设置点击按钮所在的行不可编辑
               //query_btn.click();
            })
       // console.log(pre_clickBtn)
        }

}

}
//调用
AddListener();

//给表格添加鼠标悬浮监听
function addEditlistener() {
    for(var i=1;i<td.length;i++){//表名不可修改
    td[i].onmouseover=(e)=>{
        if(chgFlag){//是否是修改状态
        //console.log(e.srcElement)
            e.srcElement.contentEditable=true;
        }
    }
    td[i].onmouseleave=(e)=>{
        if(chgFlag){//
        //console.log(e.srcElement)
           e.srcElement.contentEditable=false;
        }
    }
}
}
addEditlistener();
//这里没有用到
submit_btn.onclick=()=>{//提交按钮
    var len=th.length;
    var children=$(tr[tr.length-1]).children();
    console.log(children)
    var s={}
    s['tableVersion']=tableVersion;
    var headName=$($(tr)[1]).children();
    for(var k=0;k<len;k++){
      //name[k]=th[k].innerText;
      // value[k]=children[k].innerText;
      console.log(children[k].innerText)
      s[encodeURIComponent(headName[k].innerText)]=children[k].innerText;//{列名:属性值}
    }
    console.log(s)
     $.post('/adddata',s,(e)=>{//将s发送到客户端
       console.log(e.data)
      // query_btn.click();//触发查询点击按钮，使得页面返回查询页面

       var theLastRow=tr[tr.length-1];
	    theLastRow.contentEditable=false;//设置可编辑
	    isEdittabShowing=false;
	    add_btn.click();
    })
}
//下方查询按钮监听
document.getElementById('query_btn').onclick=()=>{
    var info=document.getElementById('query_info');
    console.log('info',info.value);
    var data={};
    data['query_info']=info.value;
    $.post(api,data,(e)=>{
        console.log(e.data)
        console.log('ok')
           // var head=e.head;
           var data1=e.data;
           // console.log(head);
           console.log(data1);
           var trLength=tr.length;
           for (var i =2;i<trLength;i++)
           {
               console.log(i)
               realtable.deleteRow(2);

           }

           // var t=realtable.insertRow(tr.length);
           // //插入表头
           // for (var i=0;i<head.length;i++){
           //     var tem=t.insertCell(i);
           //     tem.innerText=head[i][0]
           // }
           //插入表体
           for (var i=0;i<data1.length;i++){
                 var t=realtable.insertRow(tr.length);
                 for (var k=0;k<data1[i].length;k++){
                   var tem=t.insertCell(k);
                   tem.innerText=data1[i][k]
                   }
           }

    })
}
//真正的添加数据按钮
real_add_btn.onclick=()=>{

        var url='';
        var data={}
        data['length']=myinfo_panel.length;
        data['tableVersion']=tableVersion;
        data['operation']='add';//增加数据操作
        for(var i=0;i<myinfo_panel.length;i++){
            data['info_'+i]=myinfo_panel[i].value;//规定格式
        }

        $.post(api,data,(e)=>{
            console.log(e.data)
            alert(e.data)
        })

}