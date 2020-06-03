import tornado.web
import aiomysql
from sql import *
class BaseHandler(tornado.web.RequestHandler):  # 用来获取cookie，下面的鉴权注解会用到
    def get_current_user(self):
        current_user = self.get_secure_cookie('ID')
        print(current_user)
        if current_user:
            return current_user
        return None


class basicdata(BaseHandler):
    @tornado.web.authenticated
    async def get(self):
        mysql_pwd='root'
        conn = await aiomysql.connect(host='localhost', port=3306, db='船舶资料数据库', user='root', password=mysql_pwd,
                                      charset='utf8')
        cs1 = await conn.cursor()
        sqlstr='desc 船舶所有权登记证书'
        await cs1.execute(sqlstr)
        head=cs1.fetchall()

        print(head)

        await cs1.close()
        conn.close()
        username = self.get_current_user()
        self.render('BasicDataManeger.html', UserName=username,head=head)
    async def post(self):

        addstr = 'insert into 船舶所有权登记证书 values('
        querystr = 'select * from 船舶所有权登记证书 where  '
        delstr = 'delete from 船舶所有权登记证书 where 船名 = %s '

        mydb = connect()#要处理关闭问题
        length = self.get_argument('length',0)
        operation =self.get_argument('operation')#获取操作类型
        value = []
        # 获取值
        for i in range(int(length)):
            value.append(self.get_argument('info_' + str(i)))
        sqlstr=''
        if operation =='add':
            sqlstr = addstr
            for i in range(int(length)):
                if i < int(length) - 1:
                    sqlstr += '%s,'
                else:
                    sqlstr += '%s)'
            four.add(mydb, sqlstr, tuple(value))  # 第四个模块增加数据
        if operation == 'del':
            sqlstr = delstr
            del_info=self.get_argument('del_info')#要删除的船名
            retcnt = four.delete(mydb,sqlstr,str(del_info))
            if retcnt!=0:
                self.write({'code':200})
            else:
                self.write({'code': -1})

        if operation == 'query':
            sqlstr = querystr
            query_method=self.get_argument('query_method')
            query_info=self.get_argument('query_info')
            #print('query_info',query_info)
            #print('query_method', query_method)
            sqlstr=sqlstr+query_method+'= %s'
            #print(sqlstr)
            res=four.query(mydb,sqlstr,query_info)
            #print('res---',res)
            if res==None:
                self.write({'code':'-1'})
                return
            #print('查询结果--------------------------',res)
            #print(res[0])
            #print(res[0][12])
            data={}
            print(len(res[0]))
            k=0
            for i in range(len(res[0])):
                data[i]=str(res[0][i])#需要转成字符串类型
                print(data[i])
            #print(data)
            self.write({'data':data,'code':'200'})
        if operation=='mod':
            update(mydb,value)#update数据

def update(mydb,value):
    tabname='船舶所有权登记证书'
    data=four.query(mydb,'desc '+tabname)
    arg_list = []  # 获取表的列名

    for i in range(0, len(data), 1):
        arg_list.append(data[i][0])

    #print(arg_list)#查询表的属性列

    Str = "update  " + tabname + " set "  # update 语句字符串
    for i in range(0, len(arg_list), 1):  # 拼接字符串，arg_list是属性名
        Str = Str + arg_list[i] + "= %s"  # value为新的值
        if i != len(arg_list) - 1:
            Str += ","
    Str = Str + " where 船名 = %s "
    # print('arg_list',len(arg_list))
    # print('value', len(value))
    # print(Str + "-----")  # 输出字符串
    value+=value[1]   #加上查询条件船名
    # print(value)
    four.update(mydb, Str,tuple(value))  #多了个序号
