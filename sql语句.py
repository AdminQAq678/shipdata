class four_sql():
    def four_sql_query(c):
        if c=='船名':
            sql ="SELECT* FROM 船舶所有权登记证书 WHERE '船名'=%s"
        elif c=='登记号码':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '登记号码' =%s"
        elif c=='初次登记号':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '初次登记号' =%s"
        elif c=='曾用名':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '曾用名' =%s"
        elif c=='船籍港':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船籍港' =%s"
        elif c=='原船籍港':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '原船籍港' =%s"
        elif c=='船舶呼号':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船舶呼号' =%s"
        elif c=='IMO编号':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE 'IMO编号' =%s"
        elif c=='船舶种类':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船舶种类' =%s"
        elif c=='船体材料':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船体材料' =%s"
        elif c=='造船地点':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '造船地点' =%s"
        elif c=='建成日期':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '建成日期' =%s"
        elif c=='船舶价值':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船舶价值' =%s"
        elif c=='总长':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '总长' =%s"
        elif c=='型宽':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '型宽' =%s"
        elif c=='型深':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '型深' =%s"
        elif c=='总吨':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '总吨' =%s"
        elif c=='净吨':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '净吨' =%s"
        elif c=='主机种类':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '主机种类' =%s"
        elif c=='主机数目':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '主机数目' =%s"
        elif c=='功率':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '功率' =%s"
        elif c=='推进器种类':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '推进器种类' =%s"
        elif c=='推进器数目':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '推进器数目' =%s"
        elif c=='船舶所有人':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船舶所有人' =%s"
        elif c=='船舶所有人地址':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '船舶所有人地址' =%s"
        elif c=='法定代表人姓名':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '法定代表人姓名' =%s"
        elif c=='取得所有权日期':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '取得所有权日期' =%s"
        elif c=='发证机关':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '发证机关' =%s"
        elif c=='编号':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '编号' =%s"
        elif c=='发证日期':
            sql ="SELECT * FROM 船舶所有权登记证书 WHERE '发证日期' =%s"
        return sql
    def four_sql_updata(c):
        if c=='船名':
            sql ="UPDATE 船舶所有权登记证书 SET '船名'=%s WHERE '船名'=%s"
        elif c=='登记号码':
            sql ="UPDATE 船舶所有权登记证书 SET '登记号码'=%s WHERE '船名'=%s"
        elif c=='初次登记号':
            sql ="UPDATE 船舶所有权登记证书 SET '初次登记号'=%s WHERE '船名'=%s"
        elif c=='曾用名':
            sql ="UPDATE 船舶所有权登记证书 SET '曾用名'=%s WHERE '船名'=%s"
        elif c=='船籍港':
            sql ="UPDATE 船舶所有权登记证书 SET '船籍港'=%s WHERE '船名'=%s"
        elif c=='原船籍港':
            sql ="UPDATE 船舶所有权登记证书 SET '原船籍港'=%s WHERE '船名'=%s"
        elif c=='船舶呼号':
            sql ="UPDATE 船舶所有权登记证书 SET '船舶呼号'=%s WHERE '船名'=%s"
        elif c=='IMO编号':
            sql ="UPDATE 船舶所有权登记证书 SET 'IMO编号'=%s WHERE '船名'=%s"
        elif c=='船舶种类':
            sql ="UPDATE 船舶所有权登记证书 SET '船舶种类'=%s WHERE '船名'=%s"
        elif c=='船体材料':
            sql ="UPDATE 船舶所有权登记证书 SET '船体材料'=%s WHERE '船名'=%s"
        elif c=='造船地点':
            sql ="UPDATE 船舶所有权登记证书 SET '造船地点'=%s WHERE '船名'=%s"
        elif c=='建成日期':
            sql ="UPDATE 船舶所有权登记证书 SET '建成日期'=%s WHERE '船名'=%s"
        elif c=='船舶价值':
            sql ="UPDATE 船舶所有权登记证书 SET '船舶价值'=%s WHERE '船名'=%s"
        elif c=='总长':
            sql ="UPDATE 船舶所有权登记证书 SET '总长'=%s WHERE '船名'=%s"
        elif c=='型宽':
            sql ="UPDATE 船舶所有权登记证书 SET '型宽'=%s WHERE '船名'=%s"
        elif c=='型深':
            sql ="UPDATE 船舶所有权登记证书 SET '型深'=%s WHERE '船名'=%s"
        elif c=='总吨':
            sql ="UPDATE 船舶所有权登记证书 SET '总吨'=%s WHERE '船名'=%s"
        elif c=='净吨':
            sql ="UPDATE 船舶所有权登记证书 SET '净吨'=%s WHERE '船名'=%s"
        elif c=='主机种类':
            sql ="UPDATE 船舶所有权登记证书 SET '主机种类'=%s WHERE '船名'=%s"
        elif c=='主机数目':
            sql ="UPDATE 船舶所有权登记证书 SET '主机数目'=%s WHERE '船名'=%s"
        elif c=='功率':
            sql ="UPDATE 船舶所有权登记证书 SET '功率'=%s WHERE '船名'=%s"
        elif c=='推进器种类':
            sql ="UPDATE 船舶所有权登记证书 SET '推进器种类'=%s WHERE '船名'=%s"
        elif c=='推进器数目':
            sql ="UPDATE 船舶所有权登记证书 SET '推进器数目'=%s WHERE '船名'=%s"
        elif c=='船舶所有人':
            sql ="UPDATE 船舶所有权登记证书 SET '船舶所有人'=%s WHERE '船名'=%s"
        elif c=='船舶所有人地址':
            sql ="UPDATE 船舶所有权登记证书 SET '船舶所有人地址人'=%s WHERE '船名'=%s"
        elif c=='法定代表人姓名':
            sql ="UPDATE 船舶所有权登记证书 SET '法定代表人姓名人'=%s WHERE '船名'=%s"
        elif c=='取得所有权日期':
            sql ="UPDATE 船舶所有权登记证书 SET '取得所有权日期'=%s WHERE '船名'=%s"
        elif c=='发证机关':
            sql ="UPDATE 船舶所有权登记证书 SET '发证机关'=%s WHERE '船名'=%s"
        elif c=='编号':
            sql ="UPDATE 船舶所有权登记证书 SET '编号'=%s WHERE '船名'=%s"
        elif c=='发证日期':
            sql ="UPDATE 船舶所有权登记证书 SET '发证日期'=%s WHERE '船名'=%s"
        return sql

class five_sql():
    def five_sql_query(c):
        if c=='船名':
            sql ="SELECT* FROM 港澳航线船舶运营证 WHERE '船名'=%s"
        elif c=='证书编号':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '证书编号' =%s"
        elif c=='载客定额':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '载客定额' =%s"
        elif c=='载货定额':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '载货定额' =%s"
        elif c=='经济性质':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '经济性质' =%s"
        elif c=='船舶经营人':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '船舶经营人' =%s"
        elif c=='批准机关':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '批准机关' =%s"
        elif c=='批准文号':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '批准文号' =%s"
        elif c=='客运航线':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '客运航线' =%s"
        elif c=='货运航线':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '货运航线' =%s"
        elif c=='发证日期':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '发证日期' =%s"
        elif c=='有效日期':
            sql ="SELECT * FROM 港澳航线船舶运营证 WHERE '有效日期' =%s"
        return sql

    def five_sql_updata(c):
        if c=='船名':
            sql ="UPDATE 港澳航线船舶运营证 SET '船名'=%s WHERE '船名'=%s"
        elif c=='证书编号':
            sql ="UPDATE 港澳航线船舶运营证 SET '证书编号'=%s WHERE '船名'=%s"
        elif c=='载客定额':
            sql ="UPDATE 港澳航线船舶运营证 SET '载客定额'=%s WHERE '船名'=%s"
        elif c=='载货定额':
            sql ="UPDATE 港澳航线船舶运营证 SET '载货定额'=%s WHERE '船名'=%s"
        elif c=='经济性质':
            sql ="UPDATE 港澳航线船舶运营证 SET '经济性质'=%s WHERE '船名'=%s"
        elif c=='船舶经营人':
            sql ="UPDATE 港澳航线船舶运营证 SET '船舶经营人'=%s WHERE '船名'=%s"
        elif c=='批准机关':
            sql ="UPDATE 港澳航线船舶运营证 SET '批准机关'=%s WHERE '船名'=%s"
        elif c=='批准文号':
            sql ="UPDATE 港澳航线船舶运营证 SET '批准文号'=%s WHERE '船名'=%s"
        elif c=='客运航线':
            sql ="UPDATE 港澳航线船舶运营证 SET '客运航线'=%s WHERE '船名'=%s"
        elif c=='货运航线':
            sql ="UPDATE 港澳航线船舶运营证 SET '货运航线'=%s WHERE '船名'=%s"
        elif c=='发证日期':
            sql ="UPDATE 港澳航线船舶运营证 SET '发证日期'=%s WHERE '船名'=%s"
        elif c=='有效日期':
            sql ="UPDATE 港澳航线船舶运营证 SET '有效日期'=%s WHERE '船名'=%s"

        return sql
class six_sql():
    def six_sql_query(c):
        if c=='船舶名称':
            sql ="SELECT* FROM 航行港澳船舶证明书 WHERE '船舶名称'=%s"
        elif c=='证书编号':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '证书编号' =%s"
        elif c=='船员定额':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '船员定额' =%s"
        elif c=='船舶种类':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '船舶种类' =%s"
        elif c=='载重吨位':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '载重吨位' =%s"
        elif c=='船籍港':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '船籍港' =%s"
        elif c=='所属单位':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '所属单位' =%s"
        elif c=='航行有效期':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '航行有效期' =%s"
        elif c=='批复文号':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '批复文号' =%s"
        elif c=='签发机关':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '签发机关' =%s"
        elif c=='发证日期':
            sql ="SELECT * FROM 航行港澳船舶证明书 WHERE '发证日期' =%s"

        return sql

    def six_sql_updata(c):
        if c=='船舶名称':
            sql ="UPDATE 航行港澳船舶证明书 SET '船舶名称'=%s WHERE '船名'=%s"
        elif c=='证书编号':
            sql ="UPDATE 航行港澳船舶证明书 SET '证书编号'=%s WHERE '船名'=%s"
        elif c=='船员定额':
            sql ="UPDATE 航行港澳船舶证明书 SET '船员定额'=%s WHERE '船名'=%s"
        elif c=='船舶种类':
            sql ="UPDATE 航行港澳船舶证明书 SET '船舶种类'=%s WHERE '船名'=%s"
        elif c=='载重吨位':
            sql ="UPDATE 航行港澳船舶证明书 SET '载重吨位'=%s WHERE '船名'=%s"
        elif c=='船籍港':
            sql ="UPDATE 航行港澳船舶证明书 SET '船籍港'=%s WHERE '船名'=%s"
        elif c=='所属单位':
            sql ="UPDATE 航行港澳船舶证明书 SET '所属单位'=%s WHERE '船名'=%s"
        elif c=='航行有效期':
            sql ="UPDATE 航行港澳船舶证明书 SET '航行有效期'=%s WHERE '船名'=%s"
        elif c=='批复文号':
            sql ="UPDATE 航行港澳船舶证明书 SET '批复文号'=%s WHERE '船名'=%s"
        elif c=='签发机关':
            sql ="UPDATE 航行港澳船舶证明书 SET '签发机关'=%s WHERE '船名'=%s"
        elif c=='发证日期':
            sql ="UPDATE 航行港澳船舶证明书 SET '发证日期'=%s WHERE '船名'=%s"


        return sql
class seven_sql():
    def seven_sql_query(c):
        if c=='船名':
            sql ="SELECT* FROM 安全检查通知书 WHERE '船名'=%s"
        elif c=='船舶所有人':
            sql ="SELECT * FROM 安全检查通知书 WHERE '船舶所有人' =%s"
        elif c=='船舶种类':
            sql ="SELECT * FROM 安全检查通知书 WHERE '船舶种类' =%s"
        elif c=='总吨':
            sql ="SELECT * FROM 安全检查通知书 WHERE '总吨' =%s"
        elif c=='建成日期':
            sql ="SELECT * FROM 安全检查通知书 WHERE '建成日期' =%s"
        elif c=='检查日期':
            sql ="SELECT * FROM 安全检查通知书 WHERE '检查日期' =%s"
        elif c=='下次检查日期':
            sql ="SELECT * FROM 安全检查通知书 WHERE '下次检查日期' =%s"
        elif c=='检查情况':
            sql ="SELECT * FROM 安全检查通知书 WHERE '检查情况' =%s"

        return sql

    def seven_sql_updata(c):
        if c=='船名':
            sql ="UPDATE 安全检查通知书 SET '船名'=%s WHERE '船名'=%s"
        elif c=='船舶所有人':
            sql ="UPDATE 安全检查通知书 SET '船舶所有人'=%s WHERE '船名'=%s"
        elif c=='船舶种类':
            sql ="UPDATE 安全检查通知书 SET '船舶种类'=%s WHERE '船名'=%s"
        elif c=='总吨':
            sql ="UPDATE 安全检查通知书 SET '总吨'=%s WHERE '船名'=%s"
        elif c=='建成日期':
            sql ="UPDATE 安全检查通知书 SET '建成日期'=%s WHERE '船名'=%s"
        elif c=='检查日期':
            sql ="UPDATE 安全检查通知书 SET '检查日期'=%s WHERE '船名'=%s"
        elif c=='下次检查日期':
            sql ="UPDATE 安全检查通知书 SET '下次检查日期'=%s WHERE '船名'=%s"
        elif c=='检查情况':
            sql ="UPDATE 安全检查通知书 SET '检查情况'=%s WHERE '船名'=%s"


        return sql
class eight_sql():
    def eight_sql_query(c):
        if c=='船名':
            sql ="SELECT* FROM 船舶国籍证书 WHERE '船名'=%s"
        elif c=='曾用名':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '曾用名' =%s"
        elif c=='证书编号':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '证书编号' =%s"
        elif c=='证书有效期':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '证书有效期' =%s"
        elif c=='取得所有权日期':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '取得所有权日期' =%s"
        elif c=='签发日期':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '签发日期' =%s"
        elif c=='发证机关及其编号':
            sql ="SELECT * FROM 船舶国籍证书 WHERE '发证机关及其编号' =%s"


        return sql

    def eight_sql_updata(c):
        if c=='船名':
            sql ="UPDATE 船舶国籍证书 SET '船名'=%s WHERE '船名'=%s"
        elif c=='曾用名':
            sql ="UPDATE 船舶国籍证书 SET '曾用名'=%s WHERE '船名'=%s"
        elif c=='证书编号':
            sql ="UPDATE 船舶国籍证书 SET '证书编号'=%s WHERE '船名'=%s"
        elif c=='证书有效期':
            sql ="UPDATE 船舶国籍证书 SET '证书有效期'=%s WHERE '船名'=%s"
        elif c=='取得所有权日期':
            sql ="UPDATE 船舶国籍证书 SET '取得所有权日期'=%s WHERE '船名'=%s"
        elif c=='签发日期':
            sql ="UPDATE 船舶国籍证书 SET '签发日期'=%s WHERE '船名'=%s"
        elif c=='发证机关及其编号':
            sql ="UPDATE 船舶国籍证书 SET '发证机关及其编号'=%s WHERE '船名'=%s"



        return sql
class nine_sql():
    def nine_sql_query(c):
            if c=='船名':
                sql ="SELECT* FROM 航道费记录表 WHERE '船名'=%s"
            elif c=='航道费用':
                sql ="SELECT * FROM 航道费记录表 WHERE '航道费用' =%s"
            elif c=='交付日期':
                sql ="SELECT * FROM 航道费记录表 WHERE '交付日期' =%s"
            elif c=='费用有效期':
                sql ="SELECT * FROM 航道费记录表 WHERE '费用有效期' =%s"


            return sql

    def nine_sql_updata(c):
            if c=='船名':
                sql ="UPDATE 港澳航线船舶运营证 SET '船名'=%s WHERE '船名'=%s"
            elif c=='航道费用':
                sql ="UPDATE 港澳航线船舶运营证 SET '航道费用'=%s WHERE '船名'=%s"
            elif c=='交付日期':
                sql ="UPDATE 港澳航线船舶运营证 SET '交付日期'=%s WHERE '船名'=%s"
            elif c=='费用有效期':
                sql ="UPDATE 港澳航线船舶运营证 SET '费用有效期'=%s WHERE '船名'=%s"



            return sql

class ten_sql():
    def ten_sql_query(c):
                if c=='船名':
                    sql ="SELECT* FROM 航道费记录表 WHERE '船名'=%s"
                elif c=='水运费用':
                    sql ="SELECT * FROM 航道费记录表 WHERE '水运费用' =%s"
                elif c=='交付日期':
                    sql ="SELECT * FROM 航道费记录表 WHERE '交付日期' =%s"
                elif c=='缴纳月数':
                    sql ="SELECT * FROM 航道费记录表 WHERE '缴纳月数' =%s"
                elif c=='费用有效期':
                    sql ="SELECT * FROM 航道费记录表 WHERE '费用有效期' =%s"

                return sql

    def ten_sql_updata(c):
                if c=='船名':
                    sql ="UPDATE 港澳航线船舶运营证 SET '船名'=%s WHERE '船名'=%s"
                elif c=='航道费用':
                    sql ="UPDATE 港澳航线船舶运营证 SET '航道费用'=%s WHERE '船名'=%s"
                elif c=='交付日期':
                    sql ="UPDATE 港澳航线船舶运营证 SET '交付日期'=%s WHERE '船名'=%s"
                elif c=='缴纳月数':
                    sql ="UPDATE 港澳航线船舶运营证 SET '缴纳月数'=%s WHERE '船名'=%s"
                elif c=='费用有效期':
                    sql ="UPDATE 港澳航线船舶运营证 SET '费用有效期'=%s WHERE '船名'=%s"

                return sql


