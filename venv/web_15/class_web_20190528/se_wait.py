#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: se_wait
# Author: 简
# Time: 2019/5/28

from selenium import webdriver
import time

# 浏览器会话的开始
driver = webdriver.Chrome()

# 设置全局等待时间
driver.implicitly_wait(30)

driver.get("http://www.baidu.com")  # 静态页面加载完成

driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()

# 当你的操作带来了页面的变化 ，请一定要等待。
# time.sleep(5)  # 傻傻等

# 3、智能等待：明确的条件(元素可见、窗口存在。。。)。  等待+条件
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 元素存在(html里存在，能找到)、
# 元素可见(存在并且可见-看得见大小-可见才可操作)、
# 元素可用(可见之后，才有可用的可能性。只读/不可点击-不可用)

# 等待条件表达
# locator = (定位类型,定位表达式)
locator = (By.ID,'TANGRAM__PSP_10__footerULoginBtn')
# EC.visibility_of_element_located(locator)  # 条件
# 等待元素可见
WebDriverWait(driver,30).until(EC.visibility_of_element_located(locator))
# # 辅助 - 0.5秒
# time.sleep(0.5)
# 点击元素
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

# 2、智能等待：如果你10秒出现了，我就开始下一步操作。设置上限：30秒 超时TimeoutException









# 关闭当前窗口
# driver.close()

# 浏览器会话结束  关闭浏览器关闭了chromedriver
# driver.quit()
