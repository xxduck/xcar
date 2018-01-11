from sql import tables
from setting import MYSQL_CONNECT, MAX_POOL
from spider import item_list
from spider import reply_page
import logging
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from analysis import date_analysis


def item_main():
    # 例表页抓取的总入口函数
    logging.info("开始抓取item页面")
    m = tables.Mysql(MYSQL_CONNECT)
    item = item_list.Item()
    infos = item.get_info()
    err_list = []
    for info in infos:
        try:
            item_id = int(info[-2].split("tid=")[-1])
            title = info[0].replace('"', '')  # ”会影响sql语句
            poster = info[1]
            post_time = time.mktime(time.strptime(info[2], '%Y-%m-%d'))
            replies = int(info[3])
            view_count = int(info[4])
            href = info[-2]
            url = info[-1]
            print(item_id, title, poster, post_time, replies, view_count, href)
            m.insert(
                """insert into item(item_id, title, poster, post_time, replies, view_count)
            values({}, "{}", "{}", {}, {}, {});""".format(
                    item_id, title, poster, post_time, replies, view_count))

            logging.info("{}页抓取成功".format(url))
        except:
            err_list.append(info[-1])
            logging.error("{}页抓取失败".format(url))

    print(set(err_list))


reply_err = []  # 定义个错误收集器


def reply_to_mysql(tid):
    # 回复页抓取的处理函数
    m = tables.Mysql(MYSQL_CONNECT)
    r = reply_page.Reply()
    infos = r.get_info(tid)
    # 返回是一个迭代器
    sql = """insert into reply(item_id, reply_er, reply_time, reply)
        values({}, "{}", {}, "{}");"""
    try:
        # info是一个迭代器
        for info in infos:
            item_id, reply_er, reply_time, reply = info
            # 写入mysql
            m.insert(sql.format(item_id, reply_er, reply_time, reply))
            print(sql.format(item_id, reply_er, reply_time, reply))
    except:
        reply_err.append(tid)
        logging.error("{}抓取失败".format(tid))
    

def reply_main():
    # 多线程运行回复页抓取函数
    logging.info("开始抓取回复页")

    pool = ThreadPool(MAX_POOL)
    tids = tables.Mysql(MYSQL_CONNECT)

    # 只读取item_id
    sql = """select item_id from item"""
    tids = (tid['item_id'] for tid in tids.read(sql))
    pool.map(reply_to_mysql, tids)
    print(reply_err)  # 打印所有出错
    pool.close()
    pool.join()


def analysis_main():
    tids = tables.Mysql(MYSQL_CONNECT)
    analysis = date_analysis.MyJieba()
    # analysis.add_stop_word("")  添加停止词
    sql = """select reply from reply"""
    replies = tids.read(sql)
    text = ",".join((reply['reply'] for reply in replies))
    # 添加文本
    analysis.add_text(text)
    datas = list(analysis.describe())  # 是个迭代器
    # 存入mysql数据库
    sql = """insert into data(word, times, frequency, yes)
        values("{}",{}, {}, "{}")"""
    for data in datas:
        word, times, frequency, yes = data
        tids.insert(sql.format(word,times, frequency, yes))
        print(data) 

    
if __name__ == "__main__":
    item_main()  # 抓取列表页
    reply_main()  # 抓取回帖页
    analysis_main() # 分析统计词频