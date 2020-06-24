import tornado.web
import aiomysql
from sqlserver import *
mydb=conn()
class BaseHandler(tornado.web.RequestHandler):  # 用来获取cookie，下面的鉴权注解会用到
    def get_current_user(self):
        current_user = self.get_secure_cookie('ID')
        print(current_user)
        if current_user:
            return current_user
        return None

#查询资料与报表处理模块
class querydata(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_current_user()
        self.render('querydata.html', UserName=username)
    def parseToStr(self,String):
        if String==None:
            return
        print(String)
        tem=[]
        for i in String[0]:
            tem.append(str(i))
        return tem
    def post(self):
        #query_1
        # 按船只名称查询对应的各类证书：营运证书、检验证书、安检证书、国籍配员证书的基本信息
        name=self.get_argument('query_info')
        print('----name----',name)


        if name != "":

            head_1,head_2,head_3,head_4,query_data_1,query_data_2,query_data_3,query_data_4=three.query_1(mydb,name)
            print({"head_1": head_1, "head_2": head_2, "head_3": head_3, "head_4": head_4, "query_data_1": self.parseToStr(query_data_1),
                   "query_data_2": self.parseToStr(query_data_2), "query_data_3": self.parseToStr(query_data_3), "query_data_4": self.parseToStr(query_data_4)})
            self.write({"head_1": head_1, "head_2": head_2, "head_3": head_3, "head_4": head_4, "query_data_1": self.parseToStr(query_data_1),
                   "query_data_2": self.parseToStr(query_data_2), "query_data_3": self.parseToStr(query_data_3), "query_data_4": self.parseToStr(query_data_4)})

        else :
            print('查询参数为空')
        print('第一种方式查询成功')




