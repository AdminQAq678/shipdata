

print('欢迎使用船舶数据库管理系统')
import time
import urllib.request
import sys
import tornado.ioloop
import tornado.web
import hashlib
sys.path.append("BasicData.py")
sys.path.append("sql.py")
from sqlserver import *
import sql
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
mysql_pwd=u'123456'

#连接数据库
mydb=conn()
def show(self):
    global mydb
    global tabVersion
    global database
    global mysql_pwd
    cs1 = mydb.cursor()

    print('查询用户表的属性名-----------------')
    head = two.query_1(mydb)
    print(head)
    print('查询用户表的数据-------------------')
    data = two.query_2(mydb)

    cs1.execute('select  权限 from  ' + tabVersion+' where 用户ID=%s',self.get_current_user())
    priority=cs1.fetchall()
    #权限
    if(len(priority)==0):
        self.redirect('/basicdata')
    print('当前登录用户的权限：')
    print(priority[0][0])

    if priority[0][0] == '5':#判断权限是否为超级管理员
        self.render("index.html", head=head, show_list=data, tabVersion=tabVersion, UserName=self.get_current_user())
    else :
        self.redirect('/basicdata')
    cs1.close()

class MainHandler(BaseHandler):
    @tornado.web.authenticated  # 鉴权，为登录会跳转到login_url
    def get(self):
        # self.set_cookie('UserName','password',expires=time.time()+60)
        CurrentLoginUser=self.get_current_user()
        #判断cookie用户是否存在于数据库中
        if(len(two.query_2(mydb,CurrentLoginUser))==0):
            #清除当前登录的cookie
            self.clear_cookie('ID')
            #self.write('当前登录用户已过期，请重新登录')
            print('当前登录用户已过期，请重新登录')
            self.redirect('/login')
        else :
            show(self)  # 渲染页面


class deldata(tornado.web.RequestHandler):
    def post(self):
        global tabVersion
        global database
        global mysql_pwd
        # print(self.get_argument("tableName"))
        # print(self.get_argument("name"))
        tableVersion = self.get_argument("tableVersion")
        print(self.get_argument("tableVersion"))  # 获得查询的表

        cs1 = mydb.cursor()
        cs1.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name =%s ",tableVersion)
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
        print(arg_list)
        print(value)
        print(str)
        s = "delete from " + tableVersion + " where " + str + ";"
        print(s + "-----")

        print(cs1.execute(s))
        print('执行影响的条数')
        print(cs1.rowcount)
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
        print(tableVersion)

        cs1 = mydb.cursor()
        #查询用户表的属性名
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
            #url编码防止中文乱码
            value.append(self.get_argument(urllib.request.quote(arg_list[i])))
        # print(value)
        str += ")"

        #要执行的sql语句
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
            if i<len(data)-1:
                updatestr = updatestr +arg_list[i] +'=%s'+','
            else :
                updatestr= updatestr +arg_list[i]+'=%s'+' where 用户ID= %s'
        print(arg_list)

        value = []  # 保存值
        for i in arg_list:  # 获取表的列值
            value.append(self.get_argument(urllib.request.quote(i)))#url编码
        value.append(value[0])
        cs1.execute(updatestr,tuple(value))
        mydb.commit()
        if cs1.rowcount!=0:
            print(cs1.rowcount,'修改成功')
        cs1.close()
        self.write({"data": "修改成功"})

class login(tornado.web.RequestHandler):
    def get(self):
        if (self.get_secure_cookie('ID') != None):  # 当前无登录用户会返回None
            self.redirect('/')

        next_name = self.get_argument('next', '')
        code=get_validCode_img()#生成验证码，返回验证码的字母序列
        self.render('login.html', nextname=next_name,valid_code=code)

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

        #str2='select 用户ID, 密码, 员工姓名,权限 from 系统用户表 where 用户ID=%s and 密码=%s'
        cs1.execute(str,UserId)
        User = cs1.fetchall()
        print(User)
        cs1.execute(str1,UserId)
        pwd = cs1.fetchall()
        print('pwd', pwd)

        if len(User) == 0:
            print("登录失败，用户名不存在")
            self.write({'data':'登录失败，用户名不存在'})
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
        phoneNumber=self.get_argument('phoneNumber')
        UserName=self.get_argument('UserName')
        Password = hashlib.md5(Password.encode(encoding='UTF-8')).hexdigest()#加密
        print(Password)
        print('账号', UserId)
        print(Password)
        conn = pymssql.connect(host='localhost', port=1433, database='shipdata', user='root', password=mysql_pwd,
                                      charset='utf8')
        cs1 = conn.cursor()
        str = 'select * from 系统用户表 where 用户ID = %s'
        str1 = 'insert into   系统用户表 values(%s,%s,0,%s,%s)'#默认权限为0

        cs1.execute(str,UserId)
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
            cs1.execute(str1, (UserId, Password,UserName,phoneNumber))
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
        print(current_user)
        self.redirect('/login')


class chgdbandtab(tornado.web.RequestHandler):
    def post(self):
        global tabVersion
        global database
        global mysql_pwd
        tabVersion = self.get_argument('tableVersion', 'p')
        database = self.get_argument('db', 'shiyan')
        print("tab" + tabVersion)
        print("db:" + database)
        conn = pymssql.connect(host='localhost', port=1433, database=database, user='root', password=mysql_pwd,
                                      charset='utf8')
        cs1 = conn.cursor()
        cs1.execute('select  * from  ' + tabVersion)
        data = cs1.fetchall()
        cs1.execute('desc ' + tabVersion)
        head = cs1.fetchall()
        print(data)
        # cs1.execute()
        cs1.close()

        self.write({"data": data, "head": head, "tabVersion": tabVersion})

        # self.redirect('/')


class verifyPatternManeger(BaseHandler):  # 校验证书管理模块
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render('verifyPatternManeger.html', UserName=username)


class chinapatternmaneger(BaseHandler):  # 国籍配员证书管理模块
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render('chinapatternManeger.html', UserName=username)


class watertransitionfee(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render('waterTransitionFee.html', UserName=username)


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
        print(pwd[0][0])
        if pwd[0][0] != hashlib.md5(pre_pwd.encode(encoding="UTF-8")).hexdigest():  # 客户端输入的旧密码非用户真正旧密码
            self.write({'data': '旧密码输入错误'})
            print('旧密码输入错误')
        else:
            cs1.execute('update 系统用户表 set 密码 = %s where 用户ID = %s', (new_pwd, user))
            conn.commit()
            self.write({'data': '修改密码成功'})
            print('修改密码成功')
            self.clear_cookie('ID')
            pwd = cs1.fetchall()

        cs1.close()

class getValid_code(tornado.web.RequestHandler):
    def get(self):
        code=get_validCode_img()
        self.write({'data':'获取验证码成功','code':code})

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
        (r"/verifyPatternManeger", verifyPatternManeger),# 船只检验证书资料管理模块
        (r"/chinapatternmaneger", chinapatternmaneger), # 国籍配员证书管理模块
        (r"/watertransitionfee", watertransitionfee),   # 缴纳水运费情况管理模块
        (r"/chgpwd", chgpwd),
        (r"/getValid_code",getValid_code)],
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
