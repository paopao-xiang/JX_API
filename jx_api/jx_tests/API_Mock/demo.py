# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
from unittest import mock

import requests


def request_baidu():
    resp = requests.get('http://www.baidu.com')
    print(resp.text)
    print(resp.status_code)
    return resp.status_code


request_baidu = mock.Mock(return_value=500)
print(request_baidu())
