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

        conn = await aiomysql.connect(host='localhost', port=3306, db='船舶资料数据库', user='root', password='root',
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
        mydb = connect()
        length = self.get_argument('length',0)
        sqlstr = 'insert into 船舶所有权登记证书 values('
        value = []
        for i in range(int(length)):
            print(i)
            if i < int(length)-1:
               sqlstr+='%s,'
            else :
                sqlstr += '%s)'
            value.append(self.get_argument('info_' + str(i)))
        print(value)
        print(sqlstr)
        four.update(mydb,sqlstr,tuple(value))#第四个模块

        # insert
        # into
        # 船舶所有权登记证书(船名, 船舶种类, 船体材料, 机型, 船籍港, 造船地点, 船舶登记号, 营运证号, 入户时间, 迁出时间, 建成日期, 总长, 型宽, " +
        #                                                                                 "型深,总吨,净吨,功率,载重吨,航行区域,备注,船舶所有人,身份证,船舶所有人地址,联系电话) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," +
        #           "%s,%s,%s)
        pass