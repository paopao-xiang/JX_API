#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: get_shared_stus_3
# Author: liyuan
# Time: 15:53

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: 11
# Author: liyuan
# Time: 18:14

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
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
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



# 4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
# driver.find_element_by_xpath("//*[@id='return-course']").click()  # 返回班级首页
stu_loc = (By.XPATH,'//a[text()="同学"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(stu_loc))
driver.find_element(*stu_loc).click()    # 点击同学链接，进入学员页面

# 点击全部同学
all_loc = (By.XPATH,'//li[contains(@class,"all")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(all_loc))
driver.find_element(*all_loc).click()

# 学生列表 - 随机鼠标悬浮一个学生上，点击聊天标志
stu_loc = (By.XPATH,'//div[@class="all-list"]//p[@class="studentavatar"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(stu_loc)) # 等待列表元素出现
time.sleep(1)  # 有多个列表元素。第一个出现后，需要再等其它的元素出现。

stu_eles = driver.find_elements_by_xpath('//div[@class="all-list"]//li')
index = random.randint(1,len(stu_eles)-1)   # 随机学生下标
print(index)
stu_mail = stu_eles[index].find_element_by_class_name("mail").get_attribute("title") # 获取学生的title属性
print(stu_mail)
stu_eles[index].click()   # 点击学生行
time.sleep(2)
driver.save_screenshot("111.png")  # 截图

# 发消息标志框的定位表达
print('//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail))

ee = driver.find_element_by_xpath('//div[@class="all-list"]//li//p[@title="{}"]/following-sibling::a'.format(stu_mail)) # 找子元素
ActionChains(driver).move_to_element(ee).click(ee).perform()   # 鼠标操作。

#ee.click() # 点击聊天标志
# ElementNotVisibleException: Message: element not interactable

msg_loc = (By.XPATH,'//textarea[@class="ps-container"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(msg_loc))
driver.find_element(*msg_loc).send_keys("我是小姐姐，你信吗？？",Keys.CONTROL,Keys.ENTER)









