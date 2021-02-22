#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/12/25 20:55

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageLocators.bidPage_locator import BidPageLocator as loc


class BidPage:

    def __init__(self,driver):
        self.driver = driver

    # 投资
    def invest(self,money):
        # 在输入框当中，输入金额
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((loc.money_input)))
        self.driver.find_element(*loc.money_input).send_keys(money)
        #点击投标按钮
        self.driver.find_element(*loc.invest_button).click()


    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((loc.money_input)))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 投资成功的提示框 - 点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((loc.active_button_on_successPop)))
        self.driver.find_element(*loc.active_button_on_successPop).click()

    # 错误提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        # 关闭弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((loc.invest_failed_popup)))
        msg = self.driver.find_element(*loc.invest_failed_popup).text
        # 关闭弹出框
        self.driver.find_element(*loc.invest_close_failed_popup_button).click()
        return msg

    # 获取提示信息 - 投标按钮上的
    def get_errorMsg_from_investButton(self):
        pass





