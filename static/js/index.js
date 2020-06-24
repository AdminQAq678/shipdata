var query_btn=document.getElementById("query");
var add_btn=document.getElementById("add");
var del_btn=document.getElementById("del");
var mod_btn=document.getElementById("modify");
var sql="";
var delOrMod_btn;//表格右边删除按钮
var aj=new XMLHttpRequest();
var td=document.getElementsByTagName("td");//表单元格
var tr=document.getElementsByTagName("tr");//表行
var th=document.getElementsByTagName("th");//表头
var realtable=document.getElementById("realtable");//表格
var tableVersion=$("#tableVersion").children()[0].innerText;
var isEdittabShowing= false;
var chgFlag=false;
var chgdbandtabbtn=document.getElementById('chgdbandtabbtn');
for (var i=2;i<tr.length;i++){
	tr[i].innerHTML+="<button class='delOrMod_btn'hidden></button>"
}
var submit_btn=document.getElementById('submit_btn');
delOrMod_btn=document.getElementsByClassName('delOrMod_btn');
console.log(delOrMod_btn)


query_btn.onclick=()=>{

	for (var i=0;i<delOrMod_btn.length;i++){
	delOrMod_btn[i].hidden=true;
	}
	
	submit_btn.hidden=true;
    //if(isEdittabShowing) {
    ////    tr[tr.length-1].hidden=true;
   //     isEdittabShowing=false;
    //}
	//tr[tr.length-1].hidden=true;//隐藏可编辑的单元格
	$.get('/',(e)=>{
	console.log(e.data)
	    console.log("查询成功")

	})
	chgFlag=false;
}
add_btn.onclick=()=>{//添加用户按钮
	for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=true;
	}
	var cnt=0;
	for (var i=0;i<th.length;i++){
		if(tr[tr.length-1].children[i].innerText=="")
		cnt++;
		//console.log(tr[tr.length-1].children[i])
	}
	submit_btn.hidden=false;//显示提交按钮
	if(isEdittabShowing==false) {
        tr[tr.length-1].hidden=false;
        isEdittabShowing=true;
    }
	if(cnt==th.length) {//统计空白单元格个数
	    return ;
	}else{
	console.log(cnt)
	console.log(cnt)
	}
	

	var t=realtable.insertRow(tr.length );//在表格的最后一行插入
	for (var i = th.length - 1; i >= 0; i--) {
		t.insertCell(0);//插入单元格
		t.contentEditable=true;//设置可编辑
	};

	tr[tr.length-1].innerHTML+="<button class='delOrMod_btn'hidden></button>"
    chgFlag=false;
	
}
del_btn.onclick=()=>{

    option="deldata"
	for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=false;
		delOrMod_btn[i].innerText="删除"
	}
	submit_btn.hidden=true;
	 if(isEdittabShowing) {
        tr[tr.length-1].hidden=true;
        isEdittabShowing=false;
    }
    chgFlag=false;

}
mod_btn.onclick=()=>{
    option="chgdata"
	for (var i=0;i<delOrMod_btn.length;i++){
		delOrMod_btn[i].hidden=false;
		delOrMod_btn[i].innerText="修改"
	}
	submit_btn.hidden=true;
	   if(isEdittabShowing) {
        tr[tr.length-1].hidden=true;
        isEdittabShowing=false;
    }
    chgFlag=true;

}

 var option="chgdata"
for(var i=0;i< delOrMod_btn.length;i++){
    delOrMod_btn[i].onclick=function modify_opration(e){//设置修改删除按钮的监听
    var theClickedBtn=e.srcElement;
    var len=th.length;
    var children=$(e.srcElement).parent().children()
    var s={}
    //var prevalue=[];
    s['tableVersion']=tableVersion
    for(var k=0;k<len;k++){
      //使用encodeURIComponentd对传入服务器的参数名进行url编码
      //防止出现服务器无法获取到中文参数的问题
      s[encodeURIComponent(th[k].innerText)]=children[k].innerText;

    }
    console.log(s)
       $.post('/'+option,s,(e)=>{//根据option的不同去修改或者删除
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

submit_btn.onclick=()=>{//提交按钮
    var len=th.length;
    var children=$(tr[tr.length-1]).children();
    console.log(children)
    var s={}
    s['tableVersion']=tableVersion;

    for(var k=0;k<len;k++){
      //name[k]=th[k].innerText;
      // value[k]=children[k].innerText;
      console.log(children[k].innerText)
      s[encodeURIComponent(th[k].innerText)]=children[k].innerText;//{列名:属性值}
    }
    console.log(s)
     $.post('/adddata',s,(e)=>{//将s发送到客户端
       console.log(e.data)
         alert(e.data)
      // query_btn.click();//触发查询点击按钮，使得页面返回查询页面

       var theLastRow=tr[tr.length-1];
	    theLastRow.contentEditable=false;//设置可编辑
	    isEdittabShowing=false;
	    add_btn.click();
    })
}

chgdbandtabbtn.onclick=()=>{
    var dbInput=document.getElementById('dbInput');
    var tabInput=document.getElementById('tabInput');
    var s={}
    s['db']=dbInput.value;
    s['tableVersion']=tabInput.value;
    $.ajax({
        type:"POST",
        url:"/chgdbandtab",
        data:s,
        dataType:"json",
        success:function(data){
        // window.location.reload();//刷新页面
           console.log('ok')
           var head=data.head;
           var data1=data.data;
            tabVersion=data.tabVersion;
           console.log(head);
           console.log(data1);
           console.log(tabVersion);
           var trLength=tr.length;
           for (var i =1;i<trLength;i++)
           {
               console.log(i)
               realtable.deleteRow(1);

           }

           var t=realtable.insertRow(tr.length);
           //插入表头
           for (var i=0;i<head.length;i++){
               var tem=t.insertCell(i);
               tem.innerText=head[i][0]
           }
           //插入表体
           for (var i=0;i<data1.length;i++){
                 var t=realtable.insertRow(tr.length);
                 for (var k=0;k<data1[i].length;k++){
                   var tem=t.insertCell(k);
                   tem.innerText=data1[i][k]
                   }
           }
           $("#tableVersion").children()[0].innerText=tabVersion;

            // $(tableVersion).parent()

           // var t=realtable.insertRow(tr.length );//在表格的最后一行插入
           // for (var i = th.length - 1; i >= 0; i--) {
           //     t.insertCell(0);//插入单元格
           //     t.contentEditable=true;//设置可编辑
           // };

        }
    });
}