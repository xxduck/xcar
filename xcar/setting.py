"""项目配置文件"""
import pymysql.cursors


MYSQL_CONNECT = {
    'host': 'localhost',
    'user': 'xiaofang',
    'password': '123456',
    'db': 'xcar',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}