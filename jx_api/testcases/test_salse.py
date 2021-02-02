# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/6:17:49
@email:1332170414@qq.com
@function：
"""
import unittest
import string, random, json
from ddt import ddt, data
from jx_api.common import contants,logger
from jx_api.common.config import config
from jx_api.common import do_excel
from jx_api.common import do_mysql
from jx_api.common import context
from jx_api.common.http_request import HTTPRequest2
@ddt
class SalseTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'salse')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.logger.info("开始测试促销管理相关接口")
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
        params = config.get('data', 'data')
        resp = cls.http_request.request('POST', '/user/login', 'json', jsons=params)
        #将登陆的token传入header里面，后面接口调用
        cls.headers = {"content-type": "application/json", "Connection": "keep-alive", 'token': resp.json()['data']['token']}
    @data(*cases)
    def test_salse(self, case):
        case.data=context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.type, headers=self.headers,jsons=case.data)
        logger.logger.info("开始测试：{0},发送的请求是：{1},请求类型：{2}".format(case.title, case.data, type(case.data)))
        logger.logger.info("{0},返回是：{1},返回类型：{2}".format(case.title, resp.text, type(resp.text)))
        print("请求的内容：{}".format(case.title))
        if 'message' in json.loads(resp.text).keys():
            #判断返回值的类型，是否含有message提示
            try:
                self.assertEqual(str(case.expected), json.loads(resp.text)['message'])
                self.excel.write_result(case.case_id + 1, json.loads(resp.text)['message'], 'PASS')
                logger.logger.info('{0}接口测试通过'.format(case.title))
                if case.case_id == 4:
                    #将新增活动的整个返回活动id传入Context中，为下一请求的传参
                    activity_id=json.loads(resp.text)['data']['id']
                    setattr(context.Context, 'activity_id', activity_id)
                if case.case_id == 9:
                    #将新增礼品中的返回单号传入Context中，为下一请求的传参单号
                    gift_id=json.loads(resp.text)['data']['id']
                    gift_Num=json.loads(resp.text)['data']['giftNum']
                    setattr(context.Context, 'gift_id', gift_id)
                    setattr(context.Context, 'gift_Num', gift_Num)
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                logger.logger.error("报错了，{0}".format(e))
                raise e
        else:
            try:
                self.assertIsInstance(json.loads(resp.text),dict)
                self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
                logger.logger.info('{0}接口测试通过'.format(case.title))
                if case.case_id == 2:
                    #将积分申请返回的id传入Context中，为下一请求的传参
                    application_id=json.loads(resp.text)['rows'][0]['id']
                    setattr(context.Context, 'application_id', application_id)
                if case.case_id == 5:
                    #将查询的活动详情传入Context中，为下一启动活动的传参
                    body_data=json.loads(resp.text)['data']
                    setattr(context.Context, 'body_data', body_data)
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                logger.logger.error("报错了，{0}".format(e))
                raise e
    @classmethod
    def tearDownClass(cls):
        logger.logger.info('促销模块接口测试完毕')
        cls.http_request.close()
