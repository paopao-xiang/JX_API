# -*- coding:utf-8 _*-
"""
@author:paopao
@time: 2020/11/2:10:13
@email:1332170414@qq.com
@function：
"""
import urllib

import requests
from jx_api.common.config import config
from jx_api.common import logger
logger = logger.get_logger(__name__)
import json
class HTTPRequest:
    """
    独立session，cookies需要自己传递
    使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    def request(self, method, url, data=None, json=None, cookies=None):
        method = method.upper()  # 将method强制转成全大小
        if type(data) == str:
            data = eval(data)  # str转成字典
        if method == 'GET':
            resp = requests.get(url, params=data, cookies=cookies)  # resp 是Response对象
        elif method == 'POST':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            resp = None
            print('UN-support method')
        return resp


class HTTPRequest2:
    """
        公共使用一个session, cookies自动传递
       使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, paramType, jsons=None,headers=None):
        method = method.upper()  # 将method强制转成全大小
        if type(jsons) == str:
            try:
                jsons = json.loads(jsons)
            except:
                jsons = eval(jsons)
        # 拼接URL
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url:{0}'.format(url))
        logger.debug('请求data:{0}'.format(jsons))

        if paramType == 'param':
            resp = self.session.request(method=method, url=url ,headers=headers, params=jsons,verify=False)
        elif paramType == 'json':
            if json:
                resp = self.session.request(method=method, url=url, headers=headers, json=jsons,verify=False)
        else:
            resp = None
            logger.error('UN-support method')

        logger.debug('请求返回的值:{0}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()  # 用完记得关闭，很关键！！！

if __name__ == '__main__':
    http_request2 = HTTPRequest2()
    params = {"phone": "15102742565", "password": "123456"}
    resp = http_request2.request('POST', '/user/login', json=params)
    params1={"name":"customer_name","sex":"0","phone":"customer_phone","settlementType":"DAY_SETTLEMENT","type":"1","level":"0","status":"1","teceptionist":702,"default":0,"vipPoints":0,"storedValue":"1000","discount":"80","returnRate":100,"margin":5000,"maxDebt":0,"accessProtectStyle":False}
    resp1=http_request2.request('POST', '/shop/customer/saveOrUpdate', json=params1)
    http_request2.close()
    print(resp.status_code)
    print(type(resp.text))
    print(resp.json()['data']['token'])
    print(resp.json()['status'])
    print(resp.json().keys())
    print(resp.cookies)
    print(resp1.text)
    print(resp1.cookies)