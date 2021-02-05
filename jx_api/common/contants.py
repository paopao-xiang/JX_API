# -*- coding:utf-8 _*-
""" 
@author:xiangh
@time: 2018/12/17
@email:1332170414@qq.com
@function：
"""
import os
#配置相关路径

#最上层路径，jx_api
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #
#测试用例路径
case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
formal_case_file=os.path.join(base_dir, 'data', 'formal_case_file.xlsx')
#相关配置文件路径
global_file = os.path.join(base_dir, 'config', 'global.conf')
online_file = os.path.join(base_dir, 'config', 'online.conf')
test_file = os.path.join(base_dir, 'config', 'test.conf')
#日志路径
log_dir = os.path.join(base_dir, 'log')
#执行用例路径
case_dir = os.path.join(base_dir, 'testcases')
#运行结果输出路径
report_dir = os.path.join(base_dir, 'reports')


if __name__ == '__main__':
    print(case_file)
    print(formal_case_file)
    print(case_dir)