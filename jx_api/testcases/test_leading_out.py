# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/12:20:01
@email:1332170414@qq.com
@function：
"""
import unittest
import json
from ddt import ddt, data
from jx_api.common import contants
from jx_api.common import do_excel
from jx_api.common import logger
from jx_api.common.http_request import HTTPRequest2
from jx_api.common.config import config
logger = logger.get_logger(__name__)
@ddt
class LeadingOutTest(unittest.TestCase):
    excel = do_excel.DoExcel(config.get('case', 'case_file'), 'leading_out')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试导出接口')
        cls.http_request = HTTPRequest2()
        params = config.get('data', 'data')
        resp = cls.http_request.request('POST', '/user/login', 'json', jsons=params)
        # 将登陆的token传入header里面，后面接口调用
        cls.headers = {"content-type": "application/json", "Connection": "keep-alive",
                       'token': resp.json()['data']['token']}
    @data(*cases)
    def test_leading_out(self, case):
        logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_request.request(case.method, case.url, case.type, headers=self.headers, jsons=case.data)
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
        logger.info('导出接口测试完毕')
        cls.http_request.close()
