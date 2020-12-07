# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/2:10:13
@email:1332170414@qq.com
@function：
"""

"""
两种传递cookie的方式
1，单独的session，把上一个请求的返回cookies，指定传递到下一个请求的入参cookie当中
2，使用同一个session，就会自动传递cookie。
"""

import requests

session = requests.sessions.session()
# 登陆
params = {"phone":"13006364370","password":"123456"}
resp = session.request('post',
                       url='http://admin.uat.jxintell.com/user/login',
                       json=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

# 新增客户
# session2 = requests.sessions.session()
params = {"name":"customer_name","sex":"0","phone":"customer_phone","settlementType":"DAY_SETTLEMENT","type":"1","level":"0","status":"1","teceptionist":702,"default":0,"vipPoints":0,"storedValue":"1000","discount":"80","returnRate":100,"margin":5000,"maxDebt":0,"accessProtectStyle":False}
resp = session.request('post',
                       url='http://admin.uat.jxintell.com/shop/customer/saveOrUpdate',
                       json=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

session.close()  # session关闭
