#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: 按键操作
# Author: 简
# Time: 2019/6/1

# send_keys()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

from selenium.webdriver.common.keys import Keys
# 组合键的输入  Keys类
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)