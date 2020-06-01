import time
import urllib.request
import sys
import tornado.ioloop
import tornado.web
import pymysql
import aiomysql  # 异步mysql
import hashlib
sys.path.append("BasicData.py")
sys.path.append("sql.py")
import sql
from BasicData import basicdata
from BasicData import BaseHandler
# 模板语言
# 在html中{{变量名}}self.render("index.html",name="hello",li=[1,2,3])
# {% for i in li %}
# <li>{{i}}</li>
# {% end%}
database = '船舶资料数据库'
tabVersion = '船舶所有权登记证书'


async def show(self):
    global tabVersion
    global database
    conn = await aiomysql.connect(host='localhost', port=3306, db=database, user='root', password='root',
                                  charset='utf8')
    cs1 = await conn.cursor()

    await cs1.execute('show tables')
    print(cs1.fetchall())
    await cs1.execute('select  * from  ' + tabVersion)
    data = await cs1.fetchall()
    await cs1.execute('desc ' + tabVersion)
    head = await cs1.fetchall()
    print(data)
    await cs1.close()
    conn.close()
    self.render("index.html", head=head, show_list=data, tabVersion=tabVersion, UserName=self.get_current_user())




class MainHandler(BaseHandler):
    @tornado.web.authenticated  # 鉴权，为登录会跳转到login_url
    async def get(self):
        # self.set_cookie('UserName','password',expires=time.time()+60)
        await show(self)  # 渲染页面

    # self.set_cookie('hello','world')


class deldata(tornado.web.RequestHandler):
    async def post(self):

        global tabVersion
        global database
        # print(self.get_argument("tableName"))
        # print(self.get_argument("name"))
        tableVersion = self.get_argument("tableVersion")
        print(self.get_argument("tableVersion"))  # 获得查询的表
        conn = await aiomysql.connect(host='localhost', port=3306, db=database, user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor()
        await cs1.execute('desc ' + tableVersion)
        data = await cs1.fetchall()

        arg_list = []  # 保存列名
        for tem in data:
            arg_list.append(tem[0])

        value = []
        for i in arg_list:
            value.append(self.get_argument(i))
        str = ""
        for i in range(0, len(arg_list), 1):
            str = str + arg_list[i] + "='" + value[i] + "'"
            if i != len(arg_list) - 1:
                str += "&&"
        print(arg_list)
        print(value)
        print(str)
        s = "delete from " + tableVersion + " where " + str + ";"
        print(s + "-----")
        await cs1.execute(s)
        await conn.commit()
        await print(cs1.fetchall())
        await cs1.close()
        conn.close()
        self.write({"data": "删除成功"})


class adddata(tornado.web.RequestHandler):
    async def post(self):
        global tabVersion
        global database
        tableVersion = self.get_argument("tableVersion")  # 获得查询的表
        print(tableVersion)
        conn = await aiomysql.connect(host='localhost', port=3306, db=database, user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor()
        await cs1.execute('desc ' + tableVersion)
        data = await cs1.fetchall()
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



       
        for i in range(0, len(arg_list), 1):  # 获取表的列值
            str += "%s"  # 占位符，防止sql注入
            if i != len(arg_list) - 1:
                str += ','
            value.append(self.get_argument(urllib.request.quote(arg_list[i])))
        # print(value)
        str += ")"
        # print(str)
        # 拼接字符串

        # print(arg_list)
        # print(value)

        print(str + "-----")
        await cs1.execute(str, value)
        await conn.commit()
        # print(cs1.fetchall())
        await cs1.close()
        conn.close()
        self.write({"data": "添加成功"})


class chgdata(tornado.web.RequestHandler):
    async def post(self):

        global tabVersion
        global database
        tableVersion = self.get_argument("tableVersion")  # 获得查询的表
        conn = await aiomysql.connect(host='localhost', port=3306, db=database, user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor();
        await cs1.execute('desc ' + tableVersion)

        data = await cs1.fetchall()

        arg_list = []  # 获取表的列名
        print("列名")
        print(data)
        for i in range(0, len(data), 1):
            arg_list.append(data[i][0])
        print(arg_list)
        value = []  # 保存值
        for i in arg_list:  # 获取表的列值
            value.append(self.get_argument(i))
        # 拼接字符串
        pre_str = ""  # select 语句字符串，获取该行的值
        for i in range(0, len(arg_list), 1):
            pre_str = pre_str + arg_list[i] + "='" + value[i] + "'"
            if i != len(arg_list) - 1:
                pre_str += "&&"
        await cs1.execute("select *from " + tableVersion + " where " + pre_str)

        pre_value = await cs1.fetchall()
        print("select 执行结果")
        print(pre_value)

        for k in pre_value:  # 获取表中原来的值，可能会获取到多条符合条件的样本，所以可能需要执行多条update语句
            Str = "update  " + tableVersion + " set "  # update 语句字符串
            for i in range(0, len(arg_list), 1):  # 拼接字符串，arg_list是属性名
                Str = Str + arg_list[i] + "='" + value[i] + "'"  # value为新的值
                if i != len(arg_list) - 1:
                    Str += ","
            Str = Str + " where "
            for i in range(0, len(arg_list), 1):
                Str = Str + arg_list[i] + "='" + str(k[i]) + "'"  # k[i]为数据库中原先的值，这里str将值转成了字符串
                if i != len(arg_list) - 1:  # 在k[i]的两边加了"'"，将值变成了数据库中字符串，如果是数值需要另外判断处理
                    Str += "&&"
                    print(value)
            print(Str + "-----")  # 输出字符串
            cs1.execute(Str)  # 执行sql语句
            conn.commit()  # 提交
            print(cs1.fetchall())  # 获取执行结果
        await cs1.close()
        conn.close()
        self.write({"data": "修改成功"})


class login(tornado.web.RequestHandler):
    def get(self):
        if (self.get_secure_cookie('ID') != None):  # 当前无用户会返回None

            self.redirect('/')

        next_name = self.get_argument('next', '')

        self.render('login.html', nextname=next_name)

    async def post(self):
        global tabVersion
        global database

        UserId = self.get_argument("UserId", '')
        Password = self.get_argument("Password", '')
        print(UserId)
        print(Password)
        # 判断是否在数据库中存在
        # if

        # 下一个网址，也就是上一个路由地址

        conn = await aiomysql.connect(host='localhost', port=3306, db='船舶资料数据库', user='root', password='root',
                                      charset='utf8')

        cs1 = await conn.cursor()
        str = 'select 用户ID from 系统用户表 where 用户ID= %s'
        str1 = 'select 密码 from 系统用户表 where 用户ID= %s'

        #str2='select 用户ID, 密码, 员工姓名,权限 from 系统用户表 where 用户ID=%s and 密码=%s'
        await cs1.execute(str,UserId)
        User = await cs1.fetchall()
        print(User)
        await cs1.execute(str1,UserId)
        pwd = await cs1.fetchall()
        print('pwd', pwd)

        if len(User) == 0:
            self.write("登录失败，用户名不存在")
            self.redirect('/login')
            return
        # 将用户输入的密码进行MD5加密再与数据库中获取到的密码比对
        elif pwd[0][0] != hashlib.md5(Password.encode(encoding='UTF-8')).hexdigest():
            self.write({'data': "登录失败，密码不正确"})
            self.redirect('/login')
            print("登录失败，密码不正确")
            return
        await  cs1.close()
        conn.close()
        self.write({'data': "登录成功"})
        nextname = self.get_argument('next', '')
        self.set_secure_cookie('ID', UserId)
        # self.redirect('/')

    # self.write("welcome")


class register(tornado.web.RequestHandler):

    async def post(self):
        # insert
        # into
        # 系统用户表(用户ID, 密码, 权限, 员工姓名, 联系电话)
        # values(?, ?, ?, ?, ?)
        UserId = self.get_argument('UserId')
        Password = self.get_argument('Password')
        phoneNumber=self.get_argument('phoneNumber')
        UserName=self.get_argument('UserName')
        Password = hashlib.md5(Password.encode(encoding='UTF-8')).hexdigest()#加密
        print(Password)
        print('账号', UserId)
        print(Password)
        conn = await aiomysql.connect(host='localhost', port=3306, db='船舶资料数据库', user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor()
        str = 'select * from 系统用户表 where 用户ID = %s'
        str1 = 'insert into   系统用户表 values(%s,%s,0,%s,%s)'#默认权限为0

        await cs1.execute(str,UserId)
        user = await cs1.fetchall()
        print('已存在用户', user)
        nextname = self.get_argument('next', '')
        print('next', nextname)
        if len(user) != 0:
            print({'data': '注册失败，该用户已存在'})
            # self.redirect('/login')
            # self.write({'data':'注册失败'})

        else:
            print({'data': '注册成功'})
            await cs1.execute(str1, (UserId, Password,UserName,phoneNumber))
            await conn.commit()
            await cs1.execute('select * from 系统用户表')

            data = await cs1.fetchall()
            print(data)
            self.write({'data': '注册成功'})

            # self.redirect('/')

        await cs1.close()
        conn.close()

    def get(self):
        self.get_cookie()


class logout(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie('ID')
        current_user = self.get_secure_cookie('ID')
        print(current_user)
        self.redirect('/login')


class chgdbandtab(tornado.web.RequestHandler):
    async def post(self):
        global tabVersion
        global database
        tabVersion = self.get_argument('tableVersion', 'p')
        database = self.get_argument('db', 'shiyan')
        print("tab" + tabVersion)
        print("db:" + database)
        conn = await aiomysql.connect(host='localhost', port=3306, db=database, user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor()
        await cs1.execute('select  * from  ' + tabVersion)
        data = await cs1.fetchall()
        await cs1.execute('desc ' + tabVersion)
        head = await cs1.fetchall()
        print(data)
        # cs1.execute()
        await  cs1.close()
        conn.close()
        self.write({"data": data, "head": head, "tabVersion": tabVersion})

        # self.redirect('/')


class verifyPatternManeger(BaseHandler):  # 校验证书管理模块
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render('verifyPatternManeger.html', UserName=username)


# class basicdatamaneger(BaseHandler):  # 基本资料管理模块
#     @tornado.web.authenticated
#     def get(self):
#         username = self.get_current_user()
#         self.render('BasicDataManeger.html', UserName=username)


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

    async def post(self):
        pre_pwd = self.get_argument('pre_pwd')
        new_pwd = self.get_argument('new_pwd')
        new_pwd = hashlib.md5(new_pwd.encode(encoding="UTF-8")).hexdigest()
        user = self.get_secure_cookie("ID");
        conn = await aiomysql.connect(host='localhost', port=3306, db='船舶资料数据库', user='root', password='root',
                                      charset='utf8')
        cs1 = await conn.cursor()
        print(user)
        await cs1.execute('select 密码 from 系统用户表  where 用户ID = %s', user)
        pwd = await cs1.fetchall()
        print(pwd[0][0])
        if pwd[0][0] != hashlib.md5(pre_pwd.encode(encoding="UTF-8")).hexdigest():  # 客户端输入的旧密码非用户真正旧密码
            self.write({'data': '旧密码输入错误'})
            print('旧密码输入错误')
        else:
            await cs1.execute('update 系统用户表 set 密码 = %s where 用户ID = %s', (new_pwd, user))
            await conn.commit()
            self.write({'data': '修改密码成功'})
            print('修改密码成功')
            self.clear_cookie('ID')
            pwd = await cs1.fetchall()

        await cs1.close()
        conn.close()


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
        (r"/verifyPatternManeger", verifyPatternManeger),
        (r"/chinapatternmaneger", chinapatternmaneger),
        (r"/watertransitionfee", watertransitionfee),
        (r"/chgpwd", chgpwd)],
        static_path="static",
        template_path="template",
        cookie_secret='dfscmnlk2343jndjfndsfkivnd',  # cookie密码，必须要设置
        login_url='/login',
        debug=True  # 调试模式
    )


if __name__ == "__main__":
    app = make_app()

    app.listen(8787)

    tornado.ioloop.IOLoop.current().start()
