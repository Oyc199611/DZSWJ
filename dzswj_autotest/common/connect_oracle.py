# -*- coding:utf-8 -*-
"""
@Author : oyc
@Time : 2023/8/24 11:25
"""


import datetime
import cx_Oracle as Co
"""
Code description: 配置连接数据库
"""
dbinfo = {
    "host": "10.199.20.64",
    "user": "root",
    "password": "Servy0u",
    "port": 3306
}



class OracleCon:
    def __init__(self, user, password):
        # self.user = user
        # self.password = password
        self.db = Co.connect(user + '/' + password + '@10.199.20.68:1521/xjdzswjcsdb')  # 连接数据库
        self.cursor = self.db.cursor()  # 建游标

    def select(self, sql):
        # sql查询,并将结果以包含字段形式返回
        self.cursor.execute(sql)  # 执行sql
        results = self.cursor.fetchall()
        if len(results) == 0:
            print("暂未查询到数据")
        else:
            for i in results:
                list_list = list(i)
                des = self.cursor.description  # 获取表详情，字段名，长度，属性等
                t = ",".join([item[0] for item in des])
                table_head = t.split(',')  # # 查询表列名 用,分割
                dict_result = dict(zip(table_head, list_list))  # 打包为元组的列表 再转换为字典
                list_result = []
                list_result.append(dict_result)  # 将字典添加到list_result中
            return list_result

    def execute(self, sql):
        # sql 删除 提示 修改
        try:
            self.cursor.execute(sql)  # 执行sql
            self.db.commit()  # 提交修改
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        self.db.close()  # 关闭连接


def select_sql(select_sql, user, password):  # database = 具体用户
    """查询数据库"""
    db = OracleCon(user, password)
    result = db.select(select_sql)
    db.close()
    return result


def execute_sql(sql, user, password):
    """执行SQL"""
    db = OracleCon(user, password)
    db.execute(sql)
    db.close()


# if __name__ == '__main__':
    # sql = "SELECT *  FROM xt_xtcs where param_code = 'XTCS_DBSX_LX_20220516_BAK'"
    # # 结果格式 [{'XH': 20220516091200000001, 'PARAM_CODE': 'XTCS_DBSX_LX_20220516_BAK', 'PARAM_VALUE': 'WS,SB,NSRDB',
    # # 'PARAM_DESC': '我的待办查询', 'SWJG_DM': None, 'APP_CODE': None, 'PLUGIN_CODE': None, 'SENSITIVE_FIELDS': '0'}]
    # 查询语句一定要有结果，不然会报错
    # sel = select_sql(sql, 'wtjcpt', 'wtjcpt')[0]["XH"]
    # print(sel)



