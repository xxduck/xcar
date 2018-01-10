"""这是帖子回复页的抓取模块"""
from spider.base import Parent
import logging
import sys
import time
import re


class Reply(Parent):
    # def __new__(cls, *args, **kwargs):
    #     # """单例模式"""
    #     # if not hasattr(cls, "_cls"):
    #     #     cls._cls = super(Reply, cls).__new__(cls, *args, **kwargs)
    #     # return cls._cls

    def get_info(self, item_id, i=1, ):
        """从数据库获取tid构造url进行抓取，多线程逻辑由main函数负责构造"""
        self.browser.get("http://www.xcar.com.cn/bbs/viewthread.php?tid={}&page={}".format(item_id, i))
        self.my_wait("forum_coat")
        # 第一个不是帖子回复内容
        divs = self.browser.find_elements_by_class_name("F_box_2")[1:]    
        try:
            for div in divs:
                # 开头和结尾不是有效信息
                item = div.text.split('\n')
                item_id = item_id
                reply_er = item[0]
                reply_time = [i for i in item if '发表于 20' in i][0]  # 所有时间都是发表于 2017-09-05 17:02 |  来自 爱卡Android版类似格式
                # 使用正则表达式提取时间
                re_time = re.search(self.time, reply_time).group()
                time_stamp = time.mktime(time.strptime(re_time, '%Y-%m-%d'))
                reply = ','.join(item[item.index(reply_time)+1: -2]).strip()
                yield item_id, reply_er, time_stamp, reply

        except:
            logging.error("信息提取失败")
            sys.exit()

        # 有没有下一页？           
        have_next = self.browser.find_elements_by_class_name("page_down")
        if have_next:
            i += 1
            yield from self.get_info(item_id, i)
        self.browser.close()

