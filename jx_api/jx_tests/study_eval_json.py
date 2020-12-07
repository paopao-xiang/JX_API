# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：  数据类型的转换 str-->dict
"""
import json

# 正常的json格式
# {"key":[]}
params = '{"rows":200,"page":1,"filter_EQS_billNo":"PH125201105000373"}'
params1 = '{"rows":200,"page":1,"filter_EQS_billNo":"PH125201105000382"}'
  # 返回
p = '{"mobilephone":"15810447878","pwd":None}'  # 请求入参
d = eval(p)
print(d)
# json.loads()
# d = eval(params)  # 根据的python的数据类型来做转换
# print(d['status'])

d1 = json.loads(params)
d2=json.dumps(d1)
d3=json.loads(params1)
# d3=eval(params)
print(type(params))
print(type(d1), d1)
print(type(d2),d2)
# print(type(d3),d3)


d='{"page":1,"pagesize":10,"records":6,"rows":[{"id":208,"createId":"636","createDate":1604658095000,"updateId":"636","updateDate":1604658095000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":100,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":0},{"id":207,"createId":"636","createDate":1604657921000,"updateId":"636","updateDate":1604657921000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":100,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":0},{"id":206,"createId":"636","createDate":1604657469000,"updateId":"636","updateDate":1604657469000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":100,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":0},{"id":205,"createId":"636","createDate":1604654425000,"updateId":"636","updateDate":1604654425000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":1000,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":1},{"id":204,"createId":"636","createDate":1604654293000,"updateId":"636","updateDate":1604654293000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":100,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":0},{"id":200,"createId":"636","createDate":1578986190000,"updateId":"636","updateDate":1578986190000,"delFlag":false,"remark":"","createUser":null,"updateUser":null,"tenantId":"125","applicationPoints":1000,"applicationPerson":636,"applicationPersonName":"锦象","applicationChannel":253,"applicationShop":325,"shopName":"加盟管理部","approver":637,"approverName":"渠道管理员","afterPoints":null,"state":2}],"total":1,"orderByField":"createDate","obj":null,"map":null,"asc":false}'
b=json.loads(d)['rows']
print(str(b))


a='{"t":1}'
b={"t":1}
c='[123]'
print(json.loads(c))
print(eval(c))
T