# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/3:17:36
@email:1332170414@qq.com
@function：
"""
import json
import requests
from jx_api.common.write_token import OperetionJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_token(self):
        '''
        获取登录返回的token
        '''
        token = self.response['data']['token']
        # token = {"token": self.response['data']['token']}
        return token

    # 把数据写入文件
    def write_token(self):
        op_json = OperetionJson()
        op_json.write_data(self.get_response_token())

    def get_response_msg(self):
        reponse_msg = {"msg": self.response['message']}
        # print("reponse_msg:", reponse_msg)
        return reponse_msg


if __name__ == '__main__':
    from jx_api.common.http_request import  HTTPRequest2

    http_request2 = HTTPRequest2()
    params = {"phone": "15102742565", "password": "123456"}
    resp = http_request2.request('POST', '/user/login','json',jsons=params)
    resp2=resp.text
    print(resp2)
    op=OperationHeader(resp2)
    opjson = OperetionJson()
    op.write_token()
    headers = {"content-type": "application/json", "Connection": "keep-alive",'token':opjson.read_data()}
    print(headers)
    params1 = {"name": "customer_name", "sex": "0", "phone": "customer_phone", "settlementType": "DAY_SETTLEMENT",
               "type": "1", "level": "0", "status": "1", "teceptionist": 702, "default": 0, "vipPoints": 0,
               "storedValue": "1000", "discount": "80", "returnRate": 100, "margin": 5000, "maxDebt": 0,
               "accessProtectStyle": False}
    resp1 = http_request2.request('POST', '/shop/customer/saveOrUpdate' ,'json',headers=headers,jsons=params1)
    print(resp1.text)
    print(resp1.cookies)
    print(resp1.json())
    http_request2.close()