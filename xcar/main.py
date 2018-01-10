from sql import tables
from setting import MYSQL_CONNECT
from spider import item_list
import logging
import time


def item_main():
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
            m.insert("""insert into item(item_id, title, poster, post_time, replies, view_count)
            values({}, "{}", "{}", {}, {}, {});""".format(item_id, title, poster, post_time, replies, view_count))

            logging.info("{}页抓取成功".format(url))
        except:
            err_list.append(info[-1])
            logging.error("{}页抓取失败".format(url))
        
    print(err_list)



if  __name__ == "__main__":
    item_main()