# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import unittest
import string, random, json, time
from ddt import ddt, data
from jx_api.common import contants,logger
from jx_api.common.config import config
from jx_api.common import do_excel
from jx_api.common import do_mysql
from jx_api.common import context
from jx_api.common.http_request import HTTPRequest2
@ddt
class CustomerTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'customer')
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.logger.info("开始测试销售管理相关接口")
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
        params = config.get('data', 'data')
        resp = cls.http_request.request('POST', '/user/login', 'json', jsons=params)
        #将登陆的token传入header里面，后面接口调用
        cls.headers = {"content-type": "application/json", "Connection": "keep-alive", 'token': resp.json()['data']['token']}
    @data(*cases)
    def test_customer(self, case):
        case.data=context.replace(case.data)
        logger.logger.info("开始测试：{0},发送的请求是：{1},请求类型：{2}".format(case.title, case.data, type(case.data)))
        # 随机生成用户名，并且反射到Context类的属性中，方便后面参数调用
        random_str = ''.join(random.sample(string.ascii_letters, 6))
        if case.data.find('customer_name') != -1:
            case.data = case.data.replace('customer_name', random_str.lower())
            setattr(context.Context, 'customer_name', random_str)
        # 随机生成电话号码，并且反射到Context类的属性中，方便后面参数调用
        random_phone = '15' + ''.join(random.sample(string.digits, 6)) + '207'
        if case.data.find('customer_phone') != -1:
            setattr(context.Context, 'customer_phone', random_phone)
            case.data = case.data.replace('customer_phone', random_phone)
        resp = self.http_request.request(case.method, case.url, case.type, headers=self.headers,jsons=case.data)
        logger.logger.info("{0},返回是：{1},返回类型：{2}".format(case.title, resp.text, type(resp.text)))
        if 'message' in json.loads(resp.text).keys():
            #判断返回值的类型，是否含有message提示
            try:
                self.assertEqual(str(case.expected), json.loads(resp.text)['message'])
                self.excel.write_result(case.case_id + 1, json.loads(resp.text)['message'], 'PASS')
                logger.logger.info('{0}接口测试通过'.format(case.title))
                if case.case_id in (7,10):
                    #将新增单据中的返回单号传入Context中，为下一请求的传参单号
                    billNo=json.loads(resp.text)['data']['billNo']
                    #billNo=json.dumps(billNo)
                    setattr(context.Context, 'billNo', billNo)
                if case.case_id in (8,11,13):
                    #将新增单据后查询的单据详情返回值传入Context中，为下一个请求的data
                    body_data=json.loads(resp.text)['data']
                    if case.case_id == 8:
                        #如果单据出入库中的数量在详情返回值为空，需要重新赋值
                        if 'dtlList' in body_data.keys():
                            for item in body_data['dtlList']:
                                if type(item) == dict:
                                    if 'oprQty' in item.keys():
                                        item['oprQty'] = 1
                    if case.case_id ==13:
                        body_data['totInQty']=1
                    body_data = json.dumps(body_data)
                    setattr(context.Context, 'body_data', body_data)
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                logger.logger.error("报错了，{0}".format(e))
                raise e
        else:
            try:
                self.assertIsInstance(json.loads(resp.text),dict)
                self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
                logger.logger.info('{0}接口测试通过'.format(case.title))
            except AssertionError as e:
                self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
                logger.logger.error("报错了，{0}".format(e))
                raise e
    @classmethod
    def tearDownClass(cls):
        logger.logger.info('销售模块接口测试完毕')
        cls.http_request.close()
