# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/3:16:38
@email:1332170414@qq.com
@function：
"""
import json
from jx_api.common import contants
class OperetionJson:
    def __init__(self,file_path=None):
        if file_path  == None:
            self.file_path =contants.report_dir + '/token.txt'# 获取的token需要保存的地方
        else:
            self.file_path = file_path
        self.data = self.read_data()
    #读取json文件
    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as fp:
            data1 = fp.read()
            if len(data1) > 0:
                data = json.loads(data1)
            else:
                data = {}
            return data
    #根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        return self.data[id]
    #写json
    def write_data(self,data):
        with open(contants.report_dir + '/token.txt','w') as fp:
            fp.truncate()  # 先清空之前的数据，再写入，这样每次登录的token都是不一样的
            fp.write(json.dumps(data))
if __name__ == '__main__':
    opjson = OperetionJson()
    #print(opjson.get_data('shop'))
    data = {
                "user":"zhang",
                "passwd":123456
            }
    opjson.write_data(data)
    print(opjson.read_data())