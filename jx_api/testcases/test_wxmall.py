# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/23:16:29
@email:1332170414@qq.com
@function：
"""
import unittest
import string, random, json
from ddt import ddt, data
from jx_api.common import contants, logger
from jx_api.common.config import config
from jx_api.common import do_excel
from jx_api.common import do_mysql
from jx_api.common import context
from jx_api.common.http_request import HTTPRequest2


@ddt
class WxmallTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'wxMall')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.logger.info("开始商城管理相关接口")
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
        params = config.get('data', 'data')
        resp = cls.http_request.request('POST', '/user/login', 'json', jsons=params)
        # 将登陆的token传入header里面，后面接口调用
        cls.headers = {"content-type": "application/json", "Connection": "keep-alive",
                       'token': resp.json()['data']['token']}

    @data(*cases)
    def test_payment(self, case):
        case.data = context.replace(case.data)
        random_str = ''.join(random.sample(string.ascii_letters, 6))
        if case.data.find('proper_name') != -1:
            case.data = case.data.replace('proper_name', random_str.lower())
            setattr(context.Context, 'proper_name', random_str.lower())
        if case.case_id != 1:
            self.headers = {"content-type": "application/json", "Connection": "keep-alive",
                            'token': context.Context.token}
        # if case.case_id in (13,14):
        #     self.headers = {"content-type": "application/json", "Connection": "keep-alive",
        #                     'token': context.Context.token,"wxMallSecret":" a991fc5b63304cde","wxOpenId": "oOGtr1Ma5W7ZgBZecILKnfNQp3-0"}
        # 对取到的参数做解析，参数化，运用返回值传参
        logger.logger.info("开始测试：{0},发送的请求是：{1},请求类型：{2}".format(case.title, case.data, type(case.data)))
        resp = self.http_request.request(case.method, case.url, case.type, headers=self.headers, jsons=case.data)
        logger.logger.info("{0},返回是：{1},返回类型：{2}".format(case.title, resp.text, type(resp.text)))
        try:
            if 'message' in json.loads(resp.text).keys():
                # 判断返回值的类型，是否含有message提示
                try:
                    self.assertEqual(str(case.expected), json.loads(resp.text)['message'])
                    self.excel.write_result(case.case_id + 1, json.loads(resp.text)['message'], 'PASS')
                    logger.logger.info('{0}接口测试通过'.format(case.title))
                    if case.case_id == 1:
                        token = json.loads(resp.text)['data']['token']
                        setattr(context.Context, 'token', token)
                    if case.case_id in (3,6):
                        body_data = json.loads(resp.text)['data']['rows'][0]
                        if 'wxMallStyleName' in body_data.keys():
                            body_data['wxMallStyleName'] = "商城测试"
                            setattr(context.Context, 'body_data', body_data)
                        taskId = json.loads(resp.text)['data']['rows'][0]['id']
                        setattr(context.Context, 'taskId', taskId)
                    if case.case_id in (8,10):
                        taskId = json.loads(resp.text)['data']['id']
                        setattr(context.Context, 'taskId', taskId)
                except AssertionError as e:
                    self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                    logger.logger.error("报错了，{0}".format(e))
                    raise e
            else:
                try:
                    self.assertIsInstance(json.loads(resp.text), dict)
                    self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
                    logger.logger.info('{0}接口测试通过'.format(case.title))
                except AssertionError as e:
                    self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                    logger.logger.error("报错了，{0}".format(e))
                    raise e
        except:
            pass
    @classmethod
    def tearDownClass(cls):
        logger.logger.info('商城管理模块接口测试完毕')
        cls.http_request.close()
