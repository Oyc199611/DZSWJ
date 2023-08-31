# -*- coding:utf-8 -*-
"""
@Author : oyc
@Time : 2023/8/24 11:25
"""
import pymysql

"""
Code description: 配置连接数据库
"""

dbinfo = {
    "host": "10.199.20.64",
    "user": "root",
    "password": "Servy0u",
    "port": 3306
}


class DbConnect:
    def __init__(self, db_conf, database=""):
        self.db_conf = db_conf
        # 打开数据库
        self.db = pymysql.connect(database=database, cursorclass=pymysql.cursors.DictCursor, **db_conf)
        # 使用cursor()方式获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # sql查询
        self.cursor.execute(sql)  # 执行sql
        results = self.cursor.fetchall()
        return results

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


def select_sql(select_sql, database):  # database = 具体用户
    """查询数据库"""
    db = DbConnect(dbinfo, database=database)
    result = db.select(select_sql)
    db.close()
    return result


def execute_sql(sql, database):
    """执行SQL"""
    db = DbConnect(dbinfo, database=database)
    db.execute(sql)
    db.close()

# if __name__ == '__main__':
#     sql = "SELECT *  FROM xt_xtcs where param_code = 'XTCS_DBSX_LX_20220516_BAK'"
#     sel = select_sql(sql, "shjcpt")[0]["xh"]
#     print(sel)
