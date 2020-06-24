from datetime import datetime

import tornado.web
from sql import *

mydb = connect()

class BaseHandler(tornado.web.RequestHandler):  # 用来获取cookie，下面的鉴权注解会用到
    def get_current_user(self):
        current_user = self.get_secure_cookie('ID')
        print(current_user)
        if current_user:
            return current_user
        return None


class basicdata(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        cs1 = mydb.cursor()
        sqlstr = "select COLUMN_NAME from information_schema.COLUMNS where table_name =  '船舶所有权登记证书'"
        cs1.execute(sqlstr)
        head = cs1.fetchall()
        print(head)

        cs1.close()
        username = self.get_current_user()
        self.render('BasicDataManeger.html', UserName=username, head=head)
    def tran(self,date):

        if date.__contains__(':'):
            startTime = datetime.strptime(date, '%Y-%m-%d  %H:%M:%S')
        else:
            startTime = datetime.strptime(date, '%Y-%m-%d')
        print(startTime)
        return startTime
    def post(self):
        addstr = "insert into 船舶所有权登记证书(船名,登记号码,初次登记号,曾用名,船籍港,原船籍港,船舶呼号,IMO编号,船舶种类,船体材料," \
                 "造船地点,建成日期,船舶价值,总长,型宽,型深,总吨,载重,净吨,主机种类,主机数目,功率,推进器种类,推进器数目,船舶所有人," \
                 "船舶所有人地址,法定代表人姓名,取得所有权日期,发证机关,编号,发证日期) values("
        querystr = 'select * from 船舶所有权登记证书 where  '
        delstr = 'delete from 船舶所有权登记证书 where 船名 = %s '

        length = self.get_argument('length', 0)
        operation = self.get_argument('operation')  # 获取操作类型
        value = []
        # 获取值
        for i in range(int(length)):
            #print(i)
            if i==11 or i==30or i==27:
                print(self.get_argument('info_' + str(i)))
            #     value.append(self.get_argument('info_' + str(i)))
            # else:
            #     value.append(self.get_argument('info_' + str(i)))
            value.append(self.get_argument('info_' + str(i)))
        sqlstr = ''
        if operation == 'add':
            print("-----------------------------------------------")
            print(value)
            sqlstr = addstr
            for i in range(int(length)):

                if i < int(length) - 1:
                    sqlstr +="%s,"
                else:
                    sqlstr +="%s)"
            print("------------------")
            print(sqlstr)
            print(value)
            cs1=mydb.cursor()
            sqlstr="insert into 船舶所有权登记证书([船名],[登记号码],[初次登记号],[船舶种类],[船体材料],[建成日期],[总长],[型宽],[型深],[总吨],[净吨],[主机种类],[主机数目],[功率],[推进器种类],[推进器数目],[船舶所有人],[法定代表人姓名],[发证日期])" \
                   " values('1123344','1123','1123','1123','1123','1999',200,200,200,200,200,'A',3,100,'D',100,'AAA','AAA','1999')"
            #sqlstr="sp_help [船舶所有权登记证书]"
            print(sqlstr)
            cs1.execute(sqlstr)
            print(cs1.fetchall())
            #
            #four.add(mydb, sqlstr, tuple(value))  # 第四个模块增加数据
        if operation == 'del':
            sqlstr = delstr
            del_info = self.get_argument('del_info')  # 要删除的船名
            retcnt = four.delete(mydb, (sqlstr, str(del_info)))
            if retcnt != 0:
                self.write({'code': 200})
            else:
                self.write({'code': -1})

        if operation == 'query':
            sqlstr = querystr
            query_method = self.get_argument('query_method')
            query_info = self.get_argument('query_info')
            # print('query_info',query_info)
            # print('query_method', query_method)
            sqlstr = sqlstr + query_method + '= %s'
            # print(sqlstr)
            res = four.query(mydb, sqlstr,query_info)
            # print('res---',res)
            if res == None:
                self.write({'code': '-1'})
                return
            # print('查询结果--------------------------',res)
            # print(res[0])
            # print(res[0][12])
            data = {}
            print(len(res[0]))
            k = 0
            for i in range(len(res[0])):
                data[i] = str(res[0][i])  # 需要转成字符串类型
                print(data[i])
            # print(data)
            self.write({'data': data, 'code': '200'})
        if operation == 'mod':
            update(mydb, value)  # update数据




def update(mydb, value):
    tabname = '船舶所有权登记证书'
    data = four.query(mydb, 'desc ' + tabname)
    arg_list = []  # 获取表的列名

    for i in range(0, len(data), 1):
        arg_list.append(data[i][0])

    # print(arg_list)#查询表的属性列

    Str = "update  " + tabname + " set "  # update 语句字符串
    for i in range(0, len(arg_list), 1):  # 拼接字符串，arg_list是属性名
        Str = Str + arg_list[i] + "= %s"  # value为新的值
        if i != len(arg_list) - 1:
            Str += ","
    Str = Str + " where 船名 = %s "
    # print('arg_list',len(arg_list))
    # print('value', len(value))
    # print(Str + "-----")  # 输出字符串
    value += value[1]  # 加上查询条件船名
    # print(value)
    four.update(mydb, Str, tuple(value))  # 多了个序号
