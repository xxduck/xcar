"""抓取帖子列表页信息"""
from spider.base import Parent
import logging
import sys


class Item(Parent):
    """
    从html中获取标题， 发帖人，发表时间，链接等信息
    """
    def get_info(self):
        """解析html"""
        self.browser.get(self.url.format(1))
        # 计算总页数
        try:
            all_page_num = self.browser.find_elements_by_class_name("page")[-1].text  # 获取总页数
            end = int(all_page_num.strip()) + 1    # range左闭右开

        except:
            logging.error("总页数获取失败，程序退出")
            sys.exit()

        for i in range(1, end):
            url = self.url.format(i)
            self.browser.get(url)
            # 隐式等待加载完毕
            self.my_wait("list_dl")
            dls = self.browser.find_elements_by_class_name("list_dl")
            for dl in dls:
               
                # 提取每一项，用\n分割成列表
                dl_list = dl.text.split('\n')
                if len(dl_list) == 7:
                    # 长度为7的列表才是正确的信息
                    href = dl.find_elements_by_tag_name("a")[0]
                    # 把href字段合并到list
                    dl_list.append(href.get_attribute('href')) 
                    dl_list.append(url)
                    yield dl_list
 

if __name__ == "__main__":
    i = Item()
    i.get_info()
