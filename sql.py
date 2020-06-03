# import mysql.connector
import pymysql
# def connect():
#     config={'host':'127.0.0.1' or 'localhost',
#             'user':'root',
#             'password':'root',
#             'port':3306,
#             'database':'shipdata',
#             'charset':'utf8'
#             }
#     try:
#         mydb=mysql.connector.connect(**config)    #connect方法加载config的配置进行数据库的连接，完成后用一个变量进行接收
#     except mysql.connector.Error as e:
#         print('数据库链接失败！',str(e))
#     else:     #try没有异常的时候才会执行
#         print("数据库连接sucessfully!")
#         return mydb
def connect():
    mysql_pwd='root'
    mydb= pymysql.connect(host='localhost', port=3306, database='船舶资料数据库', user='root', password=mysql_pwd,
                               charset='utf8')
    return mydb


class one:   #登录信息管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class two:   #系统管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class three:   #资料查询与报表处理模块
    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

class four:   #船只基本资料管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql,val=None):      #删除
        mycursor = mydb.cursor()
        if val!=None:
            mycursor.execute(sql,val)
        else :
            mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")
        return mycursor.rowcount

    def query(mydb, sql,val=None):      #查询
        mycursor = mydb.cursor()
        if val== None :
            mycursor.execute(sql)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            return None
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class five:   #船只运营证书资料管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class six:   #船只检验证书资料管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class seven:   #船只安检证书资料管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class eight:   #船只国籍配员证书资料管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class nine:   #船只缴纳航道费情况管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

class ten:   #船只缴纳水运费情况管理模块
    def add(mydb, sql, val):      #增加
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "记录插入成功。")

    def delete(mydb, sql):      #删除
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, " 条记录删除")

    def query(mydb, sql):      #查询
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for x in myresult:
            print(x)
        print(myresult)
        if len(myresult)!=0:
            return myresult
        else:
            print("无数据")

    def update(mydb, sql, val):   #修改
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

mydb=connect()

# 实例
# ten.delete(mydb,"DELETE FROM `船舶电台执照` WHERE `序号`=2")
# ten.delete(mydb,"DELETE FROM `船舶电台执照`")
# ten.add(mydb,"INSERT INTO `船舶电台执照` (`序号`,`船名`,`呼号`,`隶属单位`,`公众通信类别`,`签发日期`,`有效期至`) VALUES (%s,%s,%s,%s,%s,%s,%s)",("2","pp","456","oo","ll","2020-05-29 10:36:37.000000","2020-05-31 10:36:41.000000"))
# ten.update(mydb,"UPDATE `船舶电台执照` SET `船名`=%s WHERE `船名`=%s",("hh","gg"))
ten.query(mydb,"SELECT* FROM `船舶电台执照`")

# 增加数据    类名.add(mydb,"INSERT INTO `表名` (`列名1`,`列名2`,.........) VALUES (%s,%s,.....)",("val1","val2",......))
# 删除数据    类名.delete(mydb,"DELETE FROM `表名` WHERE `序号`=所要删除的行的序号")      *删除某行数据
#           类名.delete(mydb,"DELETE FROM `表名`")                                    *清空表数据
# 查询数据    类名.query(mydb,"SELECT* FROM `表名`")
# 修改数据    类名.update(mydb,"UPDATE `表名` SET `列名`=%s WHERE `列名`=%s",("val","val"))    *前一个列名为修改后的值，后一个列名为需要修改的值
#



