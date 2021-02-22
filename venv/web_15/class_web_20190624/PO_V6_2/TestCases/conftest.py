#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

# fixture = 前置+后置

# 如果很多用例都有同样的前置和后置，那么我就只实现一个，然后需要的用例就去调用就好了。

# 机制：与测试用例同级，或者是测试用例的父级，创建一个conftest.py文件。
# conftest.py文件里：放所有的前置和后置。 不需要用例.py文件主动引入conftest文件。

# 模板层级：子层级可以有自己的conftest.py文件。用例优先使用自己层级的conftest。

# 怎么定义fixture?
# 定一个函数：包含前置操作+后置操作。
# 把函数声明为fixture :在函数前面加上 @pytest.fixture(作用级别=默认为function)

# 不能够与unittest兼容。

from selenium import webdriver
import pytest

from TestDatas import Comm_Datas as cd
from Common.dir_config import allure_dir
import os

from PageObjects.login_page import LoginPage

# 删除指定目录下的文件
def remove_files_in_dir(dir):
    files = os.listdir(dir)
    for item in files:
        c_path = os.path.join(dir,item)
        if os.path.isdir(c_path):
            remove_files_in_dir(c_path)
        else:
            os.remove(c_path)

# session级别的
@pytest.fixture(scope="session",autouse=True)
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除测试报告目录
    remove_files_in_dir(allure_dir)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

# 全局变量
# driver = None

# fixture的定义。如果有返回值，那么写在yield后面。
# 在测试用例当中，调用有返回值的fixture函数时，函数名称就是代表返回值。
# 在测试用例当中，函数名称作为用例的参数即可。
@pytest.fixture(scope="class")  #Base
def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.web_login_url)
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()


# 刷新页面 - 定义的第二个fixture
@pytest.fixture
def refresh_page(open_url):
    yield
    open_url.refresh()



# 在测试用例中使用fixture
# @pytest.mark.usefixtures("函数名称")
@pytest.fixture(scope="class")
def login_web(open_url):
    # 登陆操作
    LoginPage(open_url).login(cd.user,cd.passwd)
    yield open_url


# class级别的前置后置
# 投资的前置 = 打开浏览器 + 访问网址 +　登陆
# 登陆的前置 = 打开浏览器 + 访问网址
# 登陆的后置 = 关闭浏览器
# 投资的后置 = 关闭浏览器

# function级别的后置
# 登陆的后置 = 刷新网页
# 投资的后置 = 刷新网页

# 新的用例的前置后置

# fixture  - windows版本 - firefox

# unittest  - setup\teardown

# pytest - fixture (setup和teardown)-- 怎么表达的？
# 分享机制 - conftest.py
