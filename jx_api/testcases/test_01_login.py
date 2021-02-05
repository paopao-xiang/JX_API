# -*- coding:utf-8 _*-
"""
@author:paopao
@time: 2020/11/2:10:13
@email:1332170414@qq.com
@function：
"""

import unittest
import json
from ddt import ddt, data
from jx_api.common import config
from jx_api.common import do_excel
from jx_api.common import logger
from jx_api.common.http_request import HTTPRequest2
logger = logger.get_logger(__name__)
@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(config.config.get('case', 'case_file'), 'login')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试登录接口')
        cls.http_request = HTTPRequest2()
    @data(*cases)
    def test_login(self, case):
        logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_request.request(case.method, case.url, case.type, jsons=case.data)
        print("请求的内容：{}".format(case.title))
        try:
            self.assertEqual(case.expected, json.loads(resp.text)['message'])
            self.excel.write_result(case.case_id + 1, json.loads(resp.text)['message'], 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, json.loads(resp.text)['message'], 'FAIL')
            logger.error("报错了，{0}".format(e))
            raise e
        logger.info('结束测试：{0}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info('登录接口测试完毕')
        cls.http_request.close()
