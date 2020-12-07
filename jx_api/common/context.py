# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/2:10:13
@email:1332170414@qq.com
@function：
"""
import configparser
import random,string
import regex as re

from jx_api.common.config import config


class Context:
    customer_name=None
    customer_phone=None
    supplier_name=None
    supplier_phone=None
    billNo=None
    body_data=None
    color_id=None
    color_code=None
    taskId=None
    warehouse_name=None
    application_id=None
    activity_id=None
    gift_id=None
    gift_Num=None
    proper_name=None
    product_id=None
    token=None
def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(type(data))
        g = re.search(p, data).group(1)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
         # 拿到参数化的KEY
        try:
            v = config.get('data', g)  # 根据KEY取配置文件里面的值
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print('找不到参数化的值')
                raise e
        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p, str(v), data, count=1)  # 查找替换,count查找替换的次数

    return data
if __name__ == '__main__':
    data='{"name":"#customer_name#","sex":"0","phone":"#customer_phone#","settlementType":"DAY_SETTLEMENT","type":"1","level":"0","status":"1","teceptionist":702,"default":0,"vipPoints":0,"storedValue":"1000","discount":"80","returnRate":100,"margin":5000,"maxDebt":0,"accessProtectStyle":false}'
    data=replace(data)
    # 随机生成用户名，并且反射到Context类的属性中，方便后面参数调用
    random_str = ''.join(random.sample(string.ascii_letters, 6))
    if data.find('customer_name') != -1:
        setattr(Context, 'customer_name', random_str)
        print(Context.customer_name)
        data = data.replace('customer_name', random_str.lower())
    # 随机生成电话号码，并且反射到Context类的属性中，方便后面参数调用
    random_phone = '15' + ''.join(random.sample(string.digits, 6)) + '207'
    if data.find('customer_phone') != -1:
        setattr(Context, 'customer_phone', random_phone)
        data= data.replace('customer_phone', random_phone)
    print(data)
    print(type(data))