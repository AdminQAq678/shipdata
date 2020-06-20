import pymssql
from sql语句 import*
#import pyodbc
#参数注释
#name: 船名
#time: 时间（要写对时间格式，比如：2020-09-02）
#val: 赋值
#c: 选择要特定查询或修改的属性列名称（例如：'XX'）

#每个类里的修改函数中参数val包含(val,name)即修改后的值与船名，具体看sql语句


def conn():
    connect = pymssql.connect(host='localhost',server='LAPTOP-M8G6B89C\SQLEXPRESS', port='53798', user='user01', password='1044133821', database='Shipdata5')  #服务器名称，账号，密码，数据库名称
    if connect:
        print("连接成功！")
    return connect



class three():     #资料查询与报表处理模块

    def query_1(connect,name):     #按船只名称查询对应的各类证书：营运证书、检验证书、安检证书、国籍配员证书的基本信息
        cursor=connect.cursor()
        sql="SELECT* FROM 港澳航线船舶营运证,船舶最低安全配员证书,船舶国籍证书,货船适航证书 WHERE '船名'=%s"
        cursor.execute(sql,name)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def query_2(connect,name):     #按船只的名称查询该船只的缴费情况（船只的缴纳时间单位是以月为单位的）：缴纳航道费、缴纳水运费的情况；缴纳费用的历史情况；
        cursor = connect.cursor()
        sql ="SELECT* FROM 航道费记录表,水运费记录表 WHERE '船名'=%s"
        cursor.execute(sql,name)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def query_3(connect,time):      #按时间段或某一指定时间中，相关证书的有效日期和办证通知的时间等
        cursor = connect.cursor()
        sql="SELECT '证书有效期' FROM 船舶国籍证书,货船适航证书 WHERE '证书有效期'=%s SELECT '有效日期' FROM 港澳航线船舶营运证 WHERE '有效日期'=%s SELECT '证书有效期至' FROM 船舶最低安全配员证书 WHERE '证书有效期至'=%s"
        cursor.execute(sql,(time,time,time))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def query_4(connect,name):       #按船只名称查找船只的所有关联资料
        cursor = connect.cursor()
        sql ="SELECT* FROM 船舶电台执照,船舶防止油污证书,船舶共有情况,船舶国籍证书,船舶所有权登记证书,船舶相片,船舶运载危险品证书,船舶载重线证书,船舶最低安全配员证书 WHERE '船名'=%s"
        cursor.execute(sql,name)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

class four():    #船只基本资料管理模块

    def add_1(connect,val):      #录入(`编号`,`船名`,`姓名`,`性别`,`身份证号码`,`海员证号码`,`海员证到期日`,`联系电话`,`家庭联系地址`)
        cursor = connect.cursor()
        sql="INSERT INTO 船员档案 (编号,船名,姓名,性别,身份证号码,海员证号码,海员证到期日,联系电话,家庭联系地址) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def add_2(connect,val):    #录入(`船名`,`船舶所有人`,`法定代表人姓名`,`登记号码`,`初次登记号`,`船舶种类`,`船体材料`,`主机种类`,`主机数目`,`推进器种类`,`推进器数目`,`船籍港`,`造船地点`,`登记号码`,`建成日期`,`总长`,`型宽`,`型深`,`总吨`,`净吨`,`功率`,`载重`,`发证日期`)
        cursor = connect.cursor()
        sql = "INSERT INTO 船舶所有权登记证书 (船名,船舶所有人,法定代表人姓名,登记号码,初次登记号,船舶种类,船体材料,主机种类,主机数目,推进器种类,推进器数目,船籍港,造船地点,登记号码,建成日期,总长,型宽,型深,总吨,净吨,功率,载重,发证日期) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):   #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关船只的基本资料，并可以打印船只的基本资料
        cursor = connect.cursor()
        sql=four_sql.four_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):          #修改船只的基本资料并保存入数据库中
        cursor = connect.cursor()
        sql=four_sql.four_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect,name):      #从数据库中删除已经不接受管理的船只的基本资料
        cursor = connect.cursor()
        sql="DELETE FROM 船舶所有权登记证书 WHERE `船名`=%s"
        cursor.execute(sql,name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class five():        #船只营运证书资料管理模块

    def add(connect,val):        #录入(船名,证书编号,经济性质,船舶经营人,批准机关,批准文号,发证日期,有效日期)
        cursor = connect.cursor()
        sql = "INSERT INTO 港澳航线船舶营运证(船名,证书编号,经济性质,船舶经营人,批准机关,批准文号,发证日期,有效日期) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):       #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关的营运证书的基本信息
        cursor = connect.cursor()
        sql =five_sql.five_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):      #修改船只营运证书的基本信息（修改营运证到期时间等）并保存入数据库中
        cursor = connect.cursor()
        sql=five_sql.five_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect,name):         #从数据库中删除已经不接受管理的船只的营运证信息
        cursor = connect.cursor()
        sql = "DELETE FROM 港澳航线船舶营运证 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class six():    #船只检验证书资料管理模块

    def add(connect,val):        #录入(船舶名称,证书编号,船员定额,船舶种类,载重吨位,船籍港,所属单位,航行有效期,批复文号,签发机关,发证日期)
        cursor = connect.cursor()
        sql = "INSERT INTO 航行港澳船舶证明书(船舶名称,证书编号,船员定额,船舶种类,载重吨位,船籍港,所属单位,航行有效期,批复文号,签发机关,发证日期) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):       #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关的营运证书的基本信息
        cursor = connect.cursor()
        sql = six_sql.six_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):      #修改船只营运证书的基本信息（修改营运证到期时间等）并保存入数据库中
        cursor = connect.cursor()
        sql=six_sql.six_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect,name):         #从数据库中删除已经不接受管理的船只的营运证信息
        cursor = connect.cursor()
        sql = "DELETE FROM 航行港澳船舶证明书 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class seven():      #船只安检证书资料管理模块

    def add(connect,val):        #录入(船名,船舶所有人,船舶种类,总吨,建成日期,检查日期,下次检查日期,检查情况)
        cursor = connect.cursor()
        sql = "INSERT INTO 安全检查通知书(船名,船舶所有人,船舶种类,总吨,建成日期,检查日期,下次检查日期,检查情况) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):       #可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关的营运证书的基本信息
        cursor = connect.cursor()
        sql =seven_sql.seven_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):      #修改船只营运证书的基本信息（修改营运证到期时间等）并保存入数据库中
        cursor = connect.cursor()
        sql=seven_sql.seven_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect,name):         #从数据库中删除已经不接受管理的船只的营运证信息
        cursor = connect.cursor()
        sql = "DELETE FROM 安全检查通知书 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class eight():     #船只国籍配员证书资料管理模块

    def add(connect, val):      # 录入(船名,证书编号,证书有效期,取得所有权日期,签发日期,发证机关及其编号)
        cursor = connect.cursor()
        sql = "INSERT INTO 船舶国籍证书(船名,证书编号,证书有效期,取得所有权日期,签发日期,发证机关及其编号) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect, c,val):     # 可以按船只名称、船检登记号、船舶类型、船舶营运证号等进行查询相关的营运证书的基本信息
        cursor = connect.cursor()
        sql =eight_sql.eight_sql_query(c)
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):  # 修改船只营运证书的基本信息（修改营运证到期时间等）并保存入数据库中
        cursor = connect.cursor()
        sql = eight_sql.eight_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect, name):  # 从数据库中删除已经不接受管理的船只的营运证信息
        cursor = connect.cursor()
        sql = "DELETE FROM 船舶国籍证书 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class nine():       #船只缴纳航道费情况管理模块

    def add(connect, val):        #录入(船名,航道费用,交付日期,缴纳月数,费用发有效期)
        cursor = connect.cursor()
        sql = "INSERT INTO 航道费记录表(船名,航道费用,交付日期,缴纳月数,费用发有效期) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):     #按船名、本年度的各个月份、填表时间等查询相关船只缴纳航道费的记录，并可以打印查询出来的结果
        cursor = connect.cursor()
        sql = nine_sql.nine_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):     #修改船只缴纳航道费的基本情况
        cursor = connect.cursor()
        sql = nine_sql.nine_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect, name):        #删除无效船只缴纳航道费的记录
        cursor = connect.cursor()
        sql = "DELETE FROM 航道费记录表 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")

class ten():        #船只缴纳水运费情况管理模块

    def add(connect,val):         #录入(船名,水运费用,交付日期,缴纳月数,费用发有效期)
        cursor = connect.cursor()
        sql="INSERT INTO 水运费记录表(船名,水运费用,交付日期,缴纳月数,费用发有效期) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        connect.commit()
        print(cursor.rowcount, "记录插入成功。")

    def query(connect,c,val):     #按船名、本年度的各个月份、填表时间等查询相关船只缴纳水运费的记录，并可以打印查询出来的结果
        cursor = connect.cursor()
        sql = ten_sql.ten_sql_query(c)
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == True:
            return myresult
        else:
            print("无数据")

    def update(connect,c,val):      #修改船只缴纳水运费的基本情况
        cursor = connect.cursor()
        sql = ten_sql.ten_sql_updata(c)
        cursor.execute(sql,val)
        connect.commit()
        print(cursor.rowcount, " 条记录被修改")

    def delete(connect,name):       #删除无效船只缴纳水运费的记录
        cursor = connect.cursor()
        sql = "DELETE FROM 水运费记录表 WHERE `船名`=%s"
        cursor.execute(sql, name)
        connect.commit()
        print(cursor.rowcount, " 条记录删除")



