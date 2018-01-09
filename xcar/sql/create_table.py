"""mysql相关的操作"""
import pymysql
import logging


MYSQL_CONNECT = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '0805',
    # 'db': 'xcar',
    'charset': 'utf8mb4',
    'cursorclass': 'pymysql.cursors.DictCursor'
}

class Mysql(object):
    """Mysql操作"""

    def __init__(self):
        self.con = pymysql.connect(**MYSQL_CONNECT)

    def create_db(self):
        try:
            with self.con.cursor() as cursor:
                sql = "Create databases xcar" 
                cursor.execute(sql)
                cursor.close()
            self.con.commit()
        except:
            logging.error("建库出错")



