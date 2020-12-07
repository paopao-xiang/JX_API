# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/2:10:13
@email:1332170414@qq.com
@function：
"""
import unittest

from jx_api.common import HTMLTestRunnerNew
from jx_api.common import contants



discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="JX_API接口自动化测试报告",
                                              description="jx_系统升级接口测试")
    runner.run(discover)
