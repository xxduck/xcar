"""项目配置文件"""
import pymysql.cursors

# mysql连接
MYSQL_CONNECT = {
    'host': 'localhost',
    'user': 'xiaofang',
    'password': '123456',
    'db': 'xcar',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# 要开启的线程数
MAX_POOL = 2