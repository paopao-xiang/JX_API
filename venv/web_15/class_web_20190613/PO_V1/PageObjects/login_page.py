#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: login_page
# Author: 简
# Time: 2019/6/6

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PO_V1.PageLocators.login_page_locator import LoginPageLocator as loc

# 一个用例，一次浏览器的打开和结束。
class LoginPage:

    # 属性
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 登陆功能
    def login(self,user,passwd):
        # 等待？
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入用户名，输入密码，点击登陆
        self.driver.find_element(*loc.user_loc).send_keys(user)
        self.driver.find_element(*loc.passwd_loc).send_keys(passwd)
        self.driver.find_element(*loc.login_button_loc).click()


    # //div[@class="form-error-info"]
    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.error_notify_from_loginForm))
        return self.driver.find_element(*loc.error_notify_from_loginForm).text

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_notify_from_pageCenter))
        return self.driver.find_element(*loc.error_notify_from_pageCenter).text

