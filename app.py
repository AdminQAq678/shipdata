from datetime import datetime

from querydata import querydata

print('欢迎使用船舶数据库管理系统')
import urllib.request
import sys
import tornado.ioloop
import tornado.web
import hashlib

sys.path.append("BasicData.py")
sys.path.append("sql.py")
from sqlserver import *
from BasicData import basicdata
from BasicData import BaseHandler
from valide_code import *

# 模板语言
# 在html中{{变量名}}self.render("index.html",name="hello",li=[1,2,3])
# {% for i in li %}
# <li>{{i}}</li>
# {% end%}
database = u'Shipdata'
tabVersion = u'系统用户表'
mysql_pwd = u'123456'

# 连接数据库
mydb = conn()

def show(self):
    global mydb
    global tabVersion
    global database
    global mysql_pwd
    cs1 = mydb.cursor()

    # print('查询用户表的属性名-----------------')
    head = two.query_1(mydb)
    # print(head)
    # print('查询用户表的数据-------------------')
    data = two.query_2(mydb)

    cs1.execute("select  权限 from  系统用户表" + " where 用户ID=%s", self.get_current_user())
    priority = cs1.fetchall()
    # 权限
    if (len(priority) == 0):
        self.redirect('/basicdata')
    print('当前登录用户的权限：')
    print(priority[0][0])

    if priority[0][0] == '0' or priority[0][0] == '5':  # 判断权限是否为超级管理员
        self.render("index.html", head=head, show_list=data, tabVersion="系统用户表", UserName=self.get_current_user())
    else:
        self.redirect('/basicdata')
    cs1.close()


class MainHandler(BaseHandler):
    @tornado.web.authenticated  # 鉴权，为登录会跳转到login_url
    def get(self):
        # self.set_cookie('UserName','password',expires=time.time()+60)
        CurrentLoginUser = self.get_current_user()
        # 判断cookie用户是否存在于数据库中
        if two.query_2(mydb, CurrentLoginUser) == None:
            # 清除当前登录的cookie
            self.clear_cookie('ID')
            # self.write('当前登录用户已过期，请重新登录')
            print('当前登录用户已过期，请重新登录')
            self.redirect('/login')
        else:
            show(self)  # 渲染页面


class deldata(tornado.web.RequestHandler):
    def post(self):
        global tabVersion
        global database
        global mysql_pwd
        # print(self.get_argument("tableName"))
        # print(self.get_argument("name"))
        tableVersion = self.get_argument("tableVersion")
        # print(tabVersion)
        # print(self.get_argument("tableVersion"))  # 获得查询的表

        cs1 = mydb.cursor()
        cs1.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name =%s ", tableVersion)
        data = cs1.fetchall()

        arg_list = []  # 保存列名
        for tem in data:
            arg_list.append(tem[0])

        value = []
        for i in arg_list:
            value.append(self.get_argument(urllib.request.quote(i)))
        str = ""
        for i in range(0, len(arg_list), 1):
            str = str + arg_list[i] + "='" + value[i] + "'"
            if i != len(arg_list) - 1:
                str += " and "
        # print(arg_list)
        # print(value)
        # print(str)
        s = "delete from " + tableVersion + " where " + str + ";"
        # print(s + "-----")
        #
        # print(cs1.execute(s))
        # print('执行影响的条数')
        # print(cs1.rowcount)
        mydb.commit()

        cs1.close()
        self.write({"data": "删除成功"})


class adddata(tornado.web.RequestHandler):
    def post(self):
        global mydb
        global tabVersion
        global database
        global mysql_pwd
        tableVersion = self.get_argument("tableVersion")  # 获得查询的表
        # print(tableVersion)

        cs1 = mydb.cursor()
        # 查询用户表的属性名
        cs1.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name =%s ", tableVersion)
        data = cs1.fetchall()

        str = "insert into " + tableVersion + "("
        arg_list = []  # 获取表的列名
        for i in range(0, len(data), 1):
            arg_list.append(data[i][0])  # 获取列名
            str += data[i][0]
            if i != len(data) - 1:
                str += ','
        str += ") values("
        value = []

        print(arg_list)
        # 获取表的列值
        for i in range(0, len(arg_list), 1):
            str += "%s"  # 占位符，防止sql注入
            if i != len(arg_list) - 1:
                str += ','
            # url编码防止中文乱码
            value.append(self.get_argument(urllib.request.quote(arg_list[i])))
        # print(value)
        str += ")"

        # 要执行的sql语句
        print(str + "-----")
        cs1.execute(str, tuple(value))
        mydb.commit()
        print('影响的条数')
        print(cs1.rowcount)
        cs1.close()
        self.write({"data": "添加成功"})


class chgdata(tornado.web.RequestHandler):
    def post(self):
        global mydb
        global tabVersion
        global database
        global mysql_pwd
        tableVersion = self.get_argument("tableVersion")  # 获得查询的表
        cs1 = mydb.cursor()

        cs1.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name =%s ", tableVersion)

        data = cs1.fetchall()

        arg_list = []  # 获取表的列名
        # print("列名")
        # print(data)
        updatestr = 'update 系统用户表 set '
        for i in range(0, len(data), 1):
            arg_list.append(data[i][0])
            if i < len(data) - 1:
                updatestr = updatestr + arg_list[i] + '=%s' + ','
            else:
                updatestr = updatestr + arg_list[i] + '=%s' + ' where 用户ID= %s'
        print(arg_list)

        value = []  # 保存值
        for i in arg_list:  # 获取表的列值
            value.append(self.get_argument(urllib.request.quote(i)))  # url编码
        value.append(value[0])
        cs1.execute(updatestr, tuple(value))
        mydb.commit()
        if cs1.rowcount != 0:
            print(cs1.rowcount, '修改成功')
        cs1.close()
        self.write({"data": "修改成功"})


class login(tornado.web.RequestHandler):
    def get(self):
        if (self.get_secure_cookie('ID') != None):  # 当前无登录用户会返回None
            self.redirect('/')

        next_name = self.get_argument('next', '')
        code = get_validCode_img()  # 生成验证码，返回验证码的字母序列
        self.render('login.html', nextname=next_name, valid_code=code)

    def post(self):
        global tabVersion
        global database
        global mysql_pwd
        UserId = self.get_argument("UserId", '')
        Password = self.get_argument("Password", '')
        print(UserId)
        print(Password)
        # 判断是否在数据库中存在
        # if

        # 下一个网址，也就是上一个路由地址

        cs1 = mydb.cursor()
        str = 'select 用户ID from 系统用户表 where 用户ID= %s'
        str1 = 'select 密码 from 系统用户表 where 用户ID= %s'

        # str2='select 用户ID, 密码, 员工姓名,权限 from 系统用户表 where 用户ID=%s and 密码=%s'
        cs1.execute(str, UserId)
        User = cs1.fetchall()
        # print(User)
        cs1.execute(str1, UserId)
        pwd = cs1.fetchall()
        # print('pwd', pwd)

        if len(User) == 0:
            print("登录失败，用户名不存在")
            self.write({'data': '登录失败，用户名不存在'})
            return
        # 将用户输入的密码进行MD5加密再与数据库中获取到的密码比对
        elif pwd[0][0] != hashlib.md5(Password.encode(encoding='UTF-8')).hexdigest():
            self.write({'data': "登录失败，密码不正确"})
            # self.redirect('/login')
            print("登录失败，密码不正确")
            return
        cs1.close()

        self.write({'data': "登录成功"})
        nextname = self.get_argument('next', '')
        self.set_secure_cookie('ID', UserId)
        # self.redirect('/')

    # self.write("welcome")


class register(tornado.web.RequestHandler):

    def post(self):
        # insert
        # into
        # 系统用户表(用户ID, 密码, 权限, 员工姓名, 联系电话)
        # values(?, ?, ?, ?, ?)
        global mysql_pwd
        UserId = self.get_argument('UserId')
        Password = self.get_argument('Password')
        phoneNumber = self.get_argument('phoneNumber')
        UserName = self.get_argument('UserName')
        Password = hashlib.md5(Password.encode(encoding='UTF-8')).hexdigest()  # 加密
        # print('账号', UserId)
        # print(Password)
        conn = pymssql.connect(host='localhost', port=1433, database='shipdata', user='root', password=mysql_pwd,
                               charset='utf8')
        cs1 = conn.cursor()
        str = 'select * from 系统用户表 where 用户ID = %s'
        str1 = 'insert into   系统用户表 values(%s,%s,0,%s,%s)'  # 默认权限为0

        cs1.execute(str, UserId)
        user = cs1.fetchall()
        print('已存在用户', user)
        nextname = self.get_argument('next', '')
        print('next', nextname)
        if len(user) != 0:
            print({'data': '注册失败，该用户已存在'})
            # self.redirect('/login')
            # self.write({'data':'注册失败'})

        else:
            print({'data': '注册成功'})
            cs1.execute(str1, (UserId, Password, UserName, phoneNumber))
            conn.commit()
            cs1.execute('select * from 系统用户表')

            data = cs1.fetchall()
            print(data)
            self.write({'data': '注册成功'})

            # self.redirect('/')

        cs1.close()

    def get(self):
        self.get_cookie()


class logout(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie('ID')
        current_user = self.get_secure_cookie('ID')
        # print(current_user)
        self.redirect('/login')


class chgdbandtab(tornado.web.RequestHandler):
    def post(self):
        global tabVersion
        global database
        global mysql_pwd
        tabVersion = self.get_argument('tableVersion', 'p')
        database = self.get_argument('db', 'shiyan')
        # print("tab" + tabVersion)
        # print("db:" + database)
        # print('-----------------------111111111111111------------------------')
        cs1 = mydb.cursor()
        cs1.execute('select  * from  ' + tabVersion)
        data = cs1.fetchall()
        cs1.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = %s ", tabVersion)
        head = cs1.fetchall()
        # print(data)
        # print(head)
        # cs1.execute()
        cs1.close()

        self.write({"data": data, "head": head, "tabVersion": tabVersion})

        # self.redirect('/')


# 校验证书管理模块
class verifyPatternManeger(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        data = ()
        cs1 = mydb.cursor()

        # cs1.execute("select 序号,船名,船检登记号,检验证编号,船舶所有人,船舶登记号,船舶检验类型,下次检验时间,通知时间,检验机关,检验证使用有效期至,发证日期,船只检验情况记录 from 船只检验证书")
        # data=cs1.fetchall()
        # head=("序号","船名","船检登记号","检验证编号","船舶所有人","船舶登记号","船舶检验类型","下次检验时间","通知时间","检验机关","检验证使用有效期至","发证日期","船只检验情况记录")
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '锅炉检验处理历史表' "
        cs1.execute(sql)
        head = cs1.fetchall()
        cs1.execute("select *from 锅炉检验处理历史表")
        data = cs1.fetchall()
        self.render('verifyPatternManeger.html', head=head, tabVersion="锅炉检验处理历史表", show_list=data, UserName=username)

    # 删除数据使用了deldata的接口 因为
    def post(self):
        # 查询方式
        tabname = self.get_argument('tableVersion', '锅炉检验处理历史表')
        method = self.get_argument('method', 'name')  # 查询方法
        operation = self.get_argument('operation', '')  # 操作方法 查询、更新、删除
        # 录入数据
        if operation == 'add':
            tabname = self.get_argument('tableVersion', '锅炉检验处理历史表')
            sql = "insert into " + tabname + " values(%s,%s,%s,%s,%s,%s)"
            length = self.get_argument('length', 0)
            operation = self.get_argument('operation')  # 获取操作类型
            value = []
            # 获取值
            for i in range(int(length)):
                value.append(self.get_argument('info_' + str(i)))
            cs1 = mydb.cursor()
            print('sql--------------', sql)
            cs1.execute(sql, tuple(value))
            if cs1.rowcount != 0:
                self.write({'data': "添加成功"})
            else:
                self.write({'data': "添加失败"})
            print('影响的行数', cs1.rowcount)
            mydb.commit()

        elif operation == 'update':
            arg_list = ['船名', '证书编号', '办理日期', '办理人', '证书有效期至', '业务办理情况', '序号']
            value = []
            for i in arg_list:
                value.append(self.get_argument(urllib.request.quote(i)))
            sql = "update " + tabname + " set 船名 = %s,证书编号=%s ,办理日期=%s,办理人=%s,证书有效期至=%s,业务办理情况=%s where 序号=%s "
            print(sql)
            # print(value)
            cs1 = mydb.cursor()

            cs1.execute(sql, tuple(value))
            mydb.commit()
            print('影响的行数-----------', cs1.rowcount)
            if cs1.rowcount != 0:
                self.write({"data": '修改成功'})
            pass
        else:
            if method == 'all':
                cs1 = mydb.cursor()
                print('表名-------', tabname)

                cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()

                sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name =" + "'" + str(tabname) + "'"
                print('----------------', sql)
                cs1.execute(sql)
                head = cs1.fetchall()
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', res)

                data = []
                print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                print(data)
                self.write({'data': data, 'head': head})
            else:

                shipname = self.get_argument('query_info', '')

                print('---shipname---', shipname)

                tablename = '系统用户表'

                cs1 = mydb.cursor()

                if shipname != '':
                    cs1.execute("select *from " + tabname + " where 船名 = " + shipname)
                else:
                    cs1.execute("select *from  " + str(tabname))
                res = cs1.fetchall()
                data = []
                print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                print(data)
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', data)
                self.write({'data': data})
                pass


class nationCtf(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        data = ()
        cs1 = mydb.cursor()

        # cs1.execute("select 序号,船名,船检登记号,检验证编号,船舶所有人,船舶登记号,船舶检验类型,下次检验时间,通知时间,检验机关,检验证使用有效期至,发证日期,船只检验情况记录 from 船只检验证书")
        # data=cs1.fetchall()
        # head=("序号","船名","船检登记号","检验证编号","船舶所有人","船舶登记号","船舶检验类型","下次检验时间","通知时间","检验机关","检验证使用有效期至","发证日期","船只检验情况记录")
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '船舶国籍证书' "
        cs1.execute(sql)
        head = cs1.fetchall()
        cs1.execute("select *from 船舶国籍证书")
        data = cs1.fetchall()
        self.render('nationCtf.html', head=head, tabVersion="船舶国籍证书", show_list=data, UserName=username)

    def post(self):
        # 查询方式
        tabname = self.get_argument('tableVersion', '船舶国籍证书')
        method = self.get_argument('method', 'name')  # 查询方法
        operation = self.get_argument('operation', '')  # 操作方法 查询、更新、删除
        # 录入数据
        if operation == 'add':
            value = []
            # 获取值
            length = self.get_argument('length', 0)
            for i in range(int(length)):
                value.append(self.get_argument('info_' + str(i)))
            cs1 = mydb.cursor()
            sql_1 = "select *from 船舶所有权登记证书 where 船名= %s and 登记号码=%s "
            cs1.execute(sql_1, tuple(value[0:2]))
            if len(cs1.fetchall()) == 0:
                self.write({"data": "船名和登记号码不符合"})
                return

            # 1，4，5，6，7，8
            sql_2 = "insert into 船舶国籍证书(船名,证书编号,证书有效期,取得所有权日期,签发日期,发证机关及其编号) values(%s,%s,%s,%s,%s,%s)"
            tem = []
            # = value[0,3,4,5,6,7]
            tem.append(value[0])
            tem.append(value[3])
            tem.append(value[4])
            tem.append(value[5])
            tem.append(value[6])
            tem.append(value[7])
            # print(tem)
            cs1.execute(sql_2, tuple(tem))
            if cs1.rowcount != 0:
                print("sql_2执行成功")
            # 1，4,10,11,9,12
            sql_3 = "insert into  国籍证书处理历史表(船名,证书编号,办理日期,办理人,证书有效期至,业务办理情况) values(%s,%s,%s,%s,%s,%s)"

            # tem = value[0,3,9,10,8,11]
            tem = []
            tem.append(value[0])
            tem.append(value[3])
            tem.append(value[9])
            tem.append(value[10])
            tem.append(value[8])
            tem.append(value[11])
            # print('tem-------------',tem)
            cs1.execute(sql_3, tuple(tem))
            if cs1.rowcount != 0:
                print("sql_3执行成功")
            if cs1.rowcount != 0:
                self.write({'data': "添加成功"})
            else:
                self.write({'data': "添加失败"})
            print('影响的行数', cs1.rowcount)
            mydb.commit()

        elif operation == 'update':
            arg_list = ['船名', '曾用名', '证书编号', '证书有效期', '取得所有权日期', '签发日期', '发证机关及其编号', '序号']
            value = []
            for i in arg_list:
                value.append(self.get_argument(urllib.request.quote(i)))
            sql = "update 船舶国籍证书 set 船名 = %s,曾用名 = %s,证书编号=%s ,证书有效期 =%s , 取得所有权日期=%s , 签发日期= %s , 发证机关及其编号=%s  where 序号=%s "
            print(sql)
            # print(value)
            cs1 = mydb.cursor()

            cs1.execute(sql, tuple(value))
            mydb.commit()
            print('影响的行数-----------', cs1.rowcount)
            if cs1.rowcount != 0:
                self.write({"data": '修改成功'})
            pass

        elif operation == 'del':
            cs1 = mydb.cursor()

            sql = "delete from 船舶国籍证书 where 序号 =%s"
            value = self.get_argument(urllib.request.quote("序号"))
            cs1.execute(sql, value)
            mydb.commit()
            if cs1.rowcount != 0:
                print("删除成功")
                self.write({"data": "删除成功"})
            else:
                print('删除失败')
                self.write({"data": "删除失败"})
            pass
        else:
            if method == 'all':
                cs1 = mydb.cursor()
                print('表名-------', tabname)

                cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()

                sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name =" + "'" + str(tabname) + "'"
                print('----------------', sql)
                cs1.execute(sql)
                head = cs1.fetchall()
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', res)

                data = []
                print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                print(data)
                self.write({'data': data, 'head': head})
            else:
                print('-----表名------', tabname)
                shipname = self.get_argument('query_info', '')

                print('---shipname---', shipname)
                # param2=self.get_argument('query_info','');

                cs1 = mydb.cursor()

                if shipname != '':
                    cs1.execute("select *from " + tabname + " where 船名 = %s", str(shipname))
                else:
                    cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()
                data = []
                # print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                # print(data)
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', data)
                self.write({'data': data})
                pass


# 船只缴纳航道费
class navigationFee(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        html = ""
        username = self.get_current_user()
        data = ()
        cs1 = mydb.cursor()

        # cs1.execute("select 序号,船名,船检登记号,检验证编号,船舶所有人,船舶登记号,船舶检验类型,下次检验时间,通知时间,检验机关,检验证使用有效期至,发证日期,船只检验情况记录 from 船只检验证书")
        # data=cs1.fetchall()
        # head=("序号","船名","船检登记号","检验证编号","船舶所有人","船舶登记号","船舶检验类型","下次检验时间","通知时间","检验机关","检验证使用有效期至","发证日期","船只检验情况记录")
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '航道费记录表' "
        cs1.execute(sql)
        head = cs1.fetchall()
        cs1.execute("select *from 航道费记录表")
        data = cs1.fetchall()
        self.render('navigationFee.html', head=head, tabVersion="航道费记录表", show_list=data, UserName=username)

    def post(self):
        # 查询方式
        tabname = self.get_argument('tableVersion', '航道费记录表')
        method = self.get_argument('method', 'name')  # 查询方法
        operation = self.get_argument('operation', '')  # 操作方法 查询、更新、删除
        # 录入数据
        if operation == 'add':
            value = []
            # 获取值
            length = self.get_argument('length', 0)
            for i in range(int(length)):
                value.append(self.get_argument('info_' + str(i)))
            cs1 = mydb.cursor()
            sql_1 = "select *from 船舶所有权登记证书 where 船名= %s and 登记号码=%s "
            cs1.execute(sql_1, tuple(value[0:2]))
            if len(cs1.fetchall()) == 0:
                self.write({"data": "船名和登记号码不符合"})
                return

            # 1，4，5，6，7，8
            sql_2 = "insert into 航道费记录表(船名,航道费用,交付日期,缴纳月数,费用有效期) values(%s,%s,%s,%s,%s)"
            tem = []
            tem.append(value[0])
            tem.append(value[2])
            tem.append(value[3])
            tem.append(value[4])
            tem.append(value[5])

            cs1.execute(sql_2, tuple(tem))
            if cs1.rowcount != 0:
                print("sql_2执行成功")
            # 1，4,10,11,9,12
            sql_3 = "insert into  航道费有效期 (船名,费用有效期)  values(%s,%s)"

            # tem = value[0,3,9,10,8,11]
            tem = []
            tem.append(value[0])
            tem.append(value[5])
            print('tem-------------', tem)
            try:
                cs1.execute(sql_3, tuple(tem))
            except Exception:
                self.write({'data': "添加失败"})
                return
            if cs1.rowcount != 0:
                print("sql_3执行成功")
            if cs1.rowcount != 0:
                self.write({'data': "添加成功"})
            else:
                self.write({'data': "添加失败"})
            print('影响的行数', cs1.rowcount)
            mydb.commit()

        elif operation == 'update':
            arg_list = ['船名', '航道费用', '交付日期', '缴纳月数', '费用有效期', '序号']
            value = []
            for i in arg_list:
                value.append(self.get_argument(urllib.request.quote(i)))
            sql = "update 航道费记录表 set 船名 = %s,航道费用 = %s,交付日期=%s ,缴纳月数 =%s , 费用有效期=%s  where 序号=%s "
            print(sql)
            # print(value)
            cs1 = mydb.cursor()

            cs1.execute(sql, tuple(value))
            mydb.commit()
            print('影响的行数-----------', cs1.rowcount)
            if cs1.rowcount != 0:
                self.write({"data": '修改成功'})
            pass

        elif operation == 'del':
            cs1 = mydb.cursor()

            sql = "delete from 航道费记录表 where 序号 =%s"
            value = self.get_argument(urllib.request.quote("序号"))
            cs1.execute(sql, value)
            mydb.commit()
            if cs1.rowcount != 0:
                print("删除成功")
                self.write({"data": "删除成功"})
            else:
                print('删除失败')
                self.write({"data": "删除失败"})
            pass
        else:
            if method == 'all':
                cs1 = mydb.cursor()
                print('表名-------', tabname)

                cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()

                sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name =" + "'" + str(tabname) + "'"
                print('----------------', sql)
                cs1.execute(sql)
                head = cs1.fetchall()
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', res)

                data = []
                print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                print(data)
                self.write({'data': data, 'head': head})
            else:
                print('-----表名------', tabname)
                shipname = self.get_argument('query_info', '')

                print('---shipname---', shipname)
                # param2=self.get_argument('query_info','');

                cs1 = mydb.cursor()

                if shipname != '':
                    cs1.execute("select *from " + tabname + " where 船名 = %s", str(shipname))
                else:
                    cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()
                data = []
                # print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                # print(data)
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', data)
                self.write({'data': data})
                pass


# 船只缴纳水运费
class waterFee(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        cs1 = mydb.cursor()

        # cs1.execute("select 序号,船名,船检登记号,检验证编号,船舶所有人,船舶登记号,船舶检验类型,下次检验时间,通知时间,检验机关,检验证使用有效期至,发证日期,船只检验情况记录 from 船只检验证书")
        # data=cs1.fetchall()
        # head=("序号","船名","船检登记号","检验证编号","船舶所有人","船舶登记号","船舶检验类型","下次检验时间","通知时间","检验机关","检验证使用有效期至","发证日期","船只检验情况记录")
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '水运费记录表' "
        cs1.execute(sql)
        head = cs1.fetchall()
        cs1.execute("select *from 水运费记录表")
        data = cs1.fetchall()
        self.render('waterFee.html', head=head, tabVersion="水运费记录表", show_list=data, UserName=username)

    def post(self):
        # 查询方式
        tabname = self.get_argument('tableVersion', '水运费记录表')
        method = self.get_argument('method', 'name')  # 查询方法
        operation = self.get_argument('operation', '')  # 操作方法 查询、更新、删除
        # 录入数据
        if operation == 'add':
            value = []
            # 获取值
            length = self.get_argument('length', 0)
            for i in range(int(length)):
                value.append(self.get_argument('info_' + str(i)))
            cs1 = mydb.cursor()
            sql_1 = "select *from 船舶所有权登记证书 where 船名= %s and 登记号码=%s "
            cs1.execute(sql_1, tuple(value[0:2]))
            # if len(cs1.fetchall()) == 0:
            #     self.write({"data": "船名和登记号码不符合"})
            #     return
            # ss="insert into 船舶所有权登记证书(船名,登记号码,初次登记号,曾用名,船籍港,原船籍港,船舶呼号,IMO编号,船舶种类,船体材料," \
            #      "造船地点,建成日期,船舶价值,总长,型宽,型深,总吨,载重,净吨,主机种类,主机数目,功率,推进器种类,推进器数目,船舶所有人," \
            #      "船舶所有人地址,法定代表人姓名,发证机关,编号,发证日期) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
            #    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # v=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', "2020-12-13", '100', '1', '1', '12', '12', '12',
            #  '12', '1212', '12', '12', '13', '12', '12', '12', '12', '似懂非懂', '12', "2020-12-13"]
            # print(tuple(v))
            # cs1.execute(ss, tuple(v))
            # sql_x = u"insert into 船舶所有权登记证书([船名],[登记号码],[初次登记号],[船舶种类],[船体材料],[建成日期],[总长]," \
            #         "[型宽],[型深],[总吨],[净吨],[主机种类],[主机数目],[功率],[推进器种类],[推进器数目],[船舶所有人],[法定代表人姓名],[发证日期]) values(" \
            #         "'113453','1233123','1123','1123','1123','1999-11-13 12:00:00',200,200,200,200,200,'A',3,100,'D',100,'AAA','AAA','1999-11-13 12:00:00')"
            # v=['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', str(datetime.now()), 100, 1, 1, 12,  12,
            #  12, '1212', 12, 12, '13', '12', '12', '12', '12', '似懂非懂', '12', str(datetime.now())]
            # print(sql_x)
            # cs1.execute(sql_x)
            # 1，4，5，6，7，8
            sql_2 = "insert into 水运费记录表(船名,水运费用,交付日期,缴纳月数,费用有效期) values(%s,%s,%s,%s,%s)"

            tem = []
            tem.append(value[0])
            tem.append(value[2])
            tem.append(value[3])
            tem.append(value[4])
            tem.append(value[5])
            print(value[0] + value[1])
            print(tem)
            cs1.execute(sql_2, tuple(tem))
            if cs1.rowcount != 0:
                print("sql_2执行成功")
            # 1，4,10,11,9,12
            sql_3 = "insert into  水运费有效期 (船名,费用有效期)  values(%s,%s)"

            # tem = value[0,3,9,10,8,11]
            tem = []
            tem.append(value[0])
            tem.append(value[5])
            # print('tem-------------',tem)
            try:
                cs1.execute(sql_3, tuple(tem))
            except Exception:
                self.write({'data': "添加失败"})
                return
            if cs1.rowcount != 0:
                print("sql_3执行成功")
            if cs1.rowcount != 0:
                self.write({'data': "添加成功"})
            else:
                self.write({'data': "添加失败"})
            print('影响的行数', cs1.rowcount)
            mydb.commit()

        elif operation == 'update':
            arg_list = ['船名', '航道费用', '交付日期', '缴纳月数', '费用有效期', '序号']
            value = []
            for i in arg_list:
                value.append(self.get_argument(urllib.request.quote(i)))
            sql = "update 水运费记录表 set 船名 = %s,水运费用 = %s,交付日期=%s ,缴纳月数 =%s , 费用有效期=%s  where 序号=%s "
            print(sql)
            # print(value)
            cs1 = mydb.cursor()

            cs1.execute(sql, tuple(value))
            mydb.commit()
            print('影响的行数-----------', cs1.rowcount)
            if cs1.rowcount != 0:
                self.write({"data": '修改成功'})
            pass

        elif operation == 'del':
            cs1 = mydb.cursor()

            sql = "delete from 水运费记录表 where 序号 =%s"
            value = self.get_argument(urllib.request.quote("序号"))
            cs1.execute(sql, value)
            mydb.commit()
            if cs1.rowcount != 0:
                print("删除成功")
                self.write({"data": "删除成功"})
            else:
                print('删除失败')
                self.write({"data": "删除失败"})
            pass
        else:
            if method == 'all':
                cs1 = mydb.cursor()
                print('表名-------', tabname)

                cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()

                sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name =" + "'" + str(tabname) + "'"
                print('----------------', sql)
                cs1.execute(sql)
                head = cs1.fetchall()
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', res)

                data = []
                print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                print(data)
                self.write({'data': data, 'head': head})
            else:
                print('-----表名------', tabname)
                shipname = self.get_argument('query_info', '')

                print('---shipname---', shipname)
                # param2=self.get_argument('query_info','');

                cs1 = mydb.cursor()

                if shipname != '':
                    cs1.execute("select *from " + tabname + " where 船名 = %s", str(shipname))
                else:
                    cs1.execute("select *from " + str(tabname))
                res = cs1.fetchall()
                data = []
                # print('结果集大小-------', len(res))
                if (len(res) != 0):

                    for i in range(len(res)):
                        # print(res[i])

                        tem = []
                        for k in range(len(res[i])):  # 处理日期格式
                            tem.append(str(res[i][k]))
                        data.append(tem)
                # print(data)
                # print('data------------------------!!!!!!!!!!!!!!!!!!!!!!!', data)
                self.write({'data': data})
                pass


class chgpwd(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('chgpwd.html')

    def post(self):
        global mysql_pwd
        pre_pwd = self.get_argument('pre_pwd')
        new_pwd = self.get_argument('new_pwd')
        new_pwd = hashlib.md5(new_pwd.encode(encoding="UTF-8")).hexdigest()
        user = self.get_secure_cookie("ID");
        conn = pymssql.connect(host='localhost', port=1433, database='shipdata', user='root', password=mysql_pwd,
                               charset='utf8')
        cs1 = conn.cursor()
        print(user)
        cs1.execute('select 密码 from 系统用户表  where 用户ID = %s', user)
        pwd = cs1.fetchall()
        # print(pwd[0][0])
        if pwd[0][0] != hashlib.md5(pre_pwd.encode(encoding="UTF-8")).hexdigest():  # 客户端输入的旧密码非用户真正旧密码
            self.write({'data': '旧密码输入错误'})
            print('旧密码输入错误')
        else:
            cs1.execute('update 系统用户表 set 密码 = %s where 用户ID = %s', (new_pwd, user))
            conn.commit()
            self.write({'data': '修改密码成功'})
            print('修改密码成功')
            self.clear_cookie('ID')

        cs1.close()


class getValid_code(tornado.web.RequestHandler):
    def get(self):
        code = get_validCode_img()
        self.write({'data': '获取验证码成功', 'code': code})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/deldata", deldata),
        (r"/adddata", adddata),
        (r"/chgdata", chgdata),
        (r"/login", login),
        (r"/register", register),
        (r"/logout", logout),
        (r"/chgdbandtab", chgdbandtab),
        (r"/basicdata", basicdata),
        (r"/querydata", querydata),
        (r"/verifyPatternManeger", verifyPatternManeger),  # 船只检验证书资料管理模块7
        (r"/nationCtf", nationCtf),  # 国籍配员证书管理模块8
        (r"/navigationFee", navigationFee),  # 船只缴纳航道非情况管理模块9
        (r"/waterFee", waterFee),  # 缴纳水运费情况管理模块
        (r"/chgpwd", chgpwd),
        (r"/getValid_code", getValid_code)],
        static_path="static",
        template_path="template",
        cookie_secret='dfscmnlk2343jndjfndsfkivnd',  # cookie密码，必须要设置
        login_url='/login',
        debug=True  # 调试模式
    )


if __name__ == "__main__":
    app = make_app()

    app.listen(8080)

    tornado.ioloop.IOLoop.current().start()
