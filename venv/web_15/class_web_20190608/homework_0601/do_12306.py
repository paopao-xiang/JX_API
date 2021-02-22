#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: do_12306
# Author: liyuan
# Time: 15:26

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.maximize_window()
# driver.implicitly_wait(30)

driver.get('https://www.12306.cn/index/')

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'fromStationText')))
time.sleep(0.5)

# 设置起始城市
js_pha = 'var a = document.getElementById("fromStationText");a.value="上海";' \
         'var b = document.getElementById("fromStation"); b.value="SHH";'
driver.execute_script(js_pha)

# 设置终点城市
js_pha = 'document.getElementById("toStationText").value="广州";' \
         'document.getElementById("toStation").value="GZQ";'
driver.execute_script(js_pha)

# 设置日期
js_pha = 'var a = document.getElementById("train_date");a.readOnly = false;' \
         'a.value = "2019-06-15";'

driver.execute_script(js_pha)

# 发起查询
driver.find_element_by_id('search_one').click()