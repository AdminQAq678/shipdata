import pymssql

#参数注释
#T: 属性列名
#name: 船名
#time: 时间（要写对时间格式，比如：2020-09-02）
#val: 赋值


def conn():
    #connect = pymssql.connect('LAPTOP-M8G6B89C\SQLEXPRESS', 'user01', '1044133821', 'ShipData5')  #服务器名称，账号，密码，数据库名称
    connect= pymssql.connect(host='localhost', port=1433, database='Shipdata', user='root', password='123456')

    if connect:
        print("连接成功！")
    else:
        print("连接失败！")
    return connect
#查询结果函数，抽出冗余的代码
def check(cursor):
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    if len(myresult) != 0:
        return myresult
    else:
        print("无数据")
    cursor.close()

class two():
    def query_1(connect,name=None):     #系统管理模块，查询用户信息
        cursor=connect.cursor()
        #查询表的属性名
        sql="select COLUMN_NAME from information_schema.COLUMNS where table_name = '系统用户表' "
        cursor.execute(sql)
        return check(cursor)

    def query_2(connect,name=None):     #查询所有用户的所有信息
        cursor = connect.cursor()
        #分查询特定用户和查询所有用户
        if name != None:
            sql="select  * from  系统用户表 where 用户ID= %s"
            cursor.execute(sql,name)
        else :
            sql = "select  * from  系统用户表"
            cursor.execute(sql)
        return check(cursor)

class three():
    def query_1(connect,name):     #按船只名称查询对应的各类证书：营运证书、检验证书、安检证书、国籍配员证书的基本信息
        cursor=connect.cursor()
        sql="SELECT '船名' FROM 港澳航线船舶营运证,船舶最低安全配员证书,船舶国籍证书,货船适航证书 WHERE '船名'=%s"
        cursor.execute(sql,name)
        return check(cursor)

    def query_2(connect,name):     #按船只的名称查询该船只的缴费情况（船只的缴纳时间单位是以月为单位的）：缴纳航道费、缴纳水运费的情况；缴纳费用的历史情况；
        cursor = connect.cursor()
        sql ="SELECT '船名' FROM 航道费记录表,水运费记录表 WHERE '船名'=%s"
        cursor.execute(sql,name)
        return check(cursor)

    def query_3(connect,time):      #按时间段或某一指定时间中，相关证书的有效日期和办证通知的时间等
        cursor = connect.cursor()
        sql="SELECT '证书有效期' FROM 船舶国籍证书,货船适航证书 WHERE '证书有效期'=%s SELECT '有效日期' FROM 港澳航线船舶营运证 WHERE '有效日期'=%s SELECT '证书有效期至' FROM 船舶最低安全配员证书 WHERE '证书有效期至'=%s"
        cursor.execute(sql,(time,time,time))
        return check(cursor)
    def query_4(connect,name):       #按船只名称查找船只的所有关联资料
        cursor = connect.cursor()
        sql ="SELECT '船名' FROM 船舶电台执照,船舶防止油污证书,船舶共有情况,船舶国籍证书,船舶所有权登记证书,船舶相片,船舶运载危险品证书,船舶载重线证书,船舶最低安全配员证书 WHERE '船名'=%s"
        cursor.execute(sql,name)
        return check(cursor)
class four():
    def add_1(connect,val):      #录入（`编号`,`船名`,`姓名`,`身份证号码`,`联系电话`,`家庭联系地址`）
        cursor = connect.cursor()
        sql="INSERT INTO `船员档案` (`编号`,`船名`,`姓名`,`身份证号码`,`联系电话`,`家庭联系地址`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")
        cursor.close()

    def add_2(connect,val):    #录入(`船名`,`船舶种类`,`船体材料`,`主机种类`,`船籍港`,`造船地点`,`登记号码`,`建成日期`,`总长`,`型宽`,`型深`,`总吨`,`净吨`,`功率`,`载重`)
        cursor = connect.cursor()
        sql = "INSERT INTO `船舶所有权登记证` (`船名`,`船舶种类`,`船体材料`,`主机种类`,`船籍港`,`造船地点`,`登记号码`,`建成日期`,`总长`,`型宽`,`型深`,`总吨`,`净吨`,`功率`,`载重`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")
        cursor.close()

    def query(connect,T,name):   #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关船只的基本资料，并可以打印船只的基本资料
        cursor = connect.cursor()
        sql="SELECT '%s' FROM 船舶所有权登记证 WHERE '船名'=%s"
        cursor.execute(sql,T,name)
        return check(cursor)

    def update(connect,T,val,name):    #修改船只的基本资料并保存入数据库中
        cursor = connect.cursor()
        sql="UPDATE `船舶所有权登记证` SET '%s'=%s WHERE '船名'=%s"
        cursor.execute(sql,T,val,name)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")
        cursor.close()

    def delete(connect,name):      #从数据库中删除已经不接受管理的船只的基本资料
        cursor = connect.cursor()
        sql="DELETE FROM `船舶所有权登记证` WHERE `船名`=%s"
        cursor.execute(sql,name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")
        cursor.close()

class five():
    def add(connect,val):        #录入新增加的船只的营运证书的基本信息到数据库中并关联起船只名称和船检登记号：包括营运证编号、船舶所有人、船舶登记号、经营人许可证号码、管理人许可证号码、发证机关、营运证使用有效期至、发证日期
        cursor = connect.cursor()
        sql = "INSERT INTO `港澳航线船舶营运证` (`船名`,`证书编号`,`船舶经营人`,`批准机关`,`有效日期`,`发证日期`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")
        cursor.close()

    def query(connect,T,name):       #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关的营运证书的基本信息
        cursor = connect.cursor()
        sql = "SELECT '%s' FROM 船舶所有权登记证 WHERE '船名'=%s"
        cursor.execute(sql, T, name)
        return check(cursor)

    def update(connect,T,val,name):      #修改船只营运证书的基本信息（修改营运证到期时间等）并保存入数据库中
        cursor = connect.cursor()
        sql="UPDATE `港澳航线船舶营运证` SET '%s'=%s, WHERE '船名'=%s"
        cursor.execute(sql, T, val, name)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")
        cursor.close()

    def delete(connect,name):         #从数据库中删除已经不接受管理的船只的营运证信息
        cursor = connect.cursor()
        sql = "DELETE FROM `港澳航线船舶营运证` WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")
        cursor.close()



