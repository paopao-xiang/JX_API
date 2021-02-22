#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: 简
# Time: 2019/6/20

import pytest

pytest.main(["-m","demo","--alluredir=Outputs/allure_report"])

# 1、allure命令行
# 2、pytest插件、pytest命令行
# allure serve allure路径

# master-slave jdk1.6,1,8   jdk1.8  jdk1.9

# jenkins全局工具配置当中：
"""
1、jdk的版本配置
2、allure-commandline的配置
"""