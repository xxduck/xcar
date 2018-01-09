"""这是一个父模块"""
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Parent(object):
    def __init__(self):
        self.browser = webdriver.Chrome()  # 放在init方法只启动一次chrome提高效率
        self.url = "http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1774&page={}"

    def my_wait(self, who):
        """加载等待"""
        try:
            element = WebDriverWait(self.browser, 300).until(
                EC.presence_of_element_located((By.CLASS_NAME, who)))
        except:
            self.browser.quit()
            logging.error("加载失败，程序退出")
