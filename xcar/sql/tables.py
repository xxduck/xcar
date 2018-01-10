"""mysql相关的操作"""
import pymysql
import logging


class Mysql(object):
    """Mysql操作"""

    def __init__(self, setting):
        self.setting = setting
        self.con = pymysql.connect(**setting)

    def insert(self, sql):
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            self.con.commit()

        except:
            logging.error("数据库插入出错")



