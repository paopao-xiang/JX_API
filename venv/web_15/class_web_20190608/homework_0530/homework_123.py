#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: check_stu_score
# Author: liyuan
# Time: 15:51

"""
请在课堂派中实现以下操作：

0、使用帐号和密码登陆课堂派。

1、进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少

2、获取1中作业下，作业被分享的同学名称。

3、在1中，切换到作业讨论，并发表你的评论。

4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。

5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。

 【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random


driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(20)

driver.get("https://www.ketangpai.com/User/login.html")

# 0、登陆课程派
driver.find_element_by_xpath('//input[@name="account"]').send_keys("15884567545")
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("xc104070")
driver.find_element_by_xpath('//div[contains(@class,"pt-login")]//a[text()="登录"]').click()


# 等待页面某一个元素出现。等待用户id出现。
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'user')))

# 如果有公告弹框，则需要关闭公告弹框(注意弹框的id带数字，考虑id是变动的)
try:
    close_ele = driver.find_element_by_xpath('//*[contains(@class,"layui-layer-page")]//div[@class="pop-title"]//a')
except:
    pass
else:
    close_ele.click()

# 1、进入所在的班级
locator = (By.XPATH,'//div[@id="viewer-container-lists"]//a[@title="Python全栈第15期"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()

# 1.1 随机选择一个已批发的作业，查看成绩。
# 获取所有 标识为 【查看成绩】的元素。
locator = (By.XPATH,'//a[text()="查看成绩"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
score_eles = driver.find_elements(*locator)

index = random.randint(0,len(score_eles)-1)
# 随机选择一个【查看成绩】的元素进入。
score_eles[index].click()

# 1.2 查看成绩是多少
locator = (By.XPATH,'//p[contains(@class,"score")]//span')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
score = driver.find_element(*locator).text
print("随机找的一个作业，作业成绩为：{}".format(score))



# 2、获取1中作业下，作业被分享的同学名称。
stu_eles = driver.find_elements_by_xpath('//p[@class="share-name"]')
print("本次作业被分享的学员昵称为：")
for ele in stu_eles:
    print(ele.text)


# 3、在1中，切换到作业讨论，并发表你的评论。
driver.find_element_by_xpath('//a[text()="作业讨论"]').click()  # 切换到作业讨论
locator = (By.XPATH,'//div[contains(@class,"input-click")]')  # 点击，出现输入区域
WebDriverWait(driver,20).until(EC.visibility_of_element_located(locator))
driver.find_element(*locator).click()   # 出现输入区域

comment_loc = (By.XPATH,'//textarea[@class="comment-txt"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(comment_loc))
driver.find_element(*comment_loc).send_keys("作业已提交了，哦耶！！")  # 输入评语
driver.find_element_by_xpath('//div[@class="add-comment"]//a[text()="确定"]').click()   # 点击确定，提交
