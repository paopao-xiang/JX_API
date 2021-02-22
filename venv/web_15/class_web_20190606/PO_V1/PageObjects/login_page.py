#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: 简
# Time: 2019/6/6

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 一个用例，一次浏览器的打开和结束。
class LoginPage:

    # 属性
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 登陆功能
    def login(self,user,passwd):
        # 等待？
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="phone"]')))
        # 输入用户名，输入密码，点击登陆
        self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys(user)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button').click()


    # def input_user(self):
    #     pass
    #
    # def input_passwd(self):
    #     pass
    #
    # def click_login_button(self):
    #     pass