#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: index_page
# Author: 简
# Time: 2019/6/6

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.indexPage_locator import IndexPageLocator as loc
import time

class IndexPage:

    def __init__(self,driver):
        self.driver = driver

    # 检测昵称是否存在
    def check_nick_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        #// a[text() = "关于我们"]
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located(loc.about_us))
        time.sleep(0.5)
        try:
            self.driver.find_element(*loc.user_link)
            return True
        except:
            return False

    # 点击投标按钮
    def click_invest_button(self):
        pass

