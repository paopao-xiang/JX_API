#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 简
# Time: 2019/6/6

import unittest
from selenium import webdriver
from class_web_20190606.PO_V1.PageObjects.login_page import LoginPage
from class_web_20190606.PO_V1.PageObjects.index_page import IndexPage

# 用例三步曲：前置 、步骤 、 断言
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 前置 - 打开网页。启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")

    def tearDown(self):
        self.driver.quit()


    # 正常用例 - 登陆+首页
    def test_login_success(self):
        # 步骤 - 登陆操作 - 登陆页面 - 18684720553、python
        LoginPage(self.driver).login("18684720553","python")  # 测试对象+测试数据
        # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists()) # 测试对象+测试数据
        # url跳转
        self.assertEqual(self.driver.current_url,"http://120.78.128.25:8765/Index/index") # 测试对象+测试数据


    # # 异常用例 - 无密码
    # def test_login_failed_by_no_passwd(self):
    #     # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
    #     # 断言 - 页面的提示内容为：请输入密码
    #     pass

