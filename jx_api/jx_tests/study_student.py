# -*- coding:utf-8 _*-
""" 
@author:paopao
@time: 2020/11/25:16:31
@email:1332170414@qq.com
@function：
"""
import re
class StudentManmge:
    def __init__(self):
        self.l_student=[]
    def add_student(self):
        #录入学生资料的方法
        item =int(input("请输入需要录入的学生人数:(正整数)"))
        #获取需要录入的学生人数
        if item > 0:
            for t in range(item):
                d_student = {}
                d_student['name']=input("请输入姓名:")
                d_student['tel']=input("请输入手机号:")
                d_student['qq']=input("请输入QQ:")
                d_student['id']=len(self.l_student)+1
                while len(d_student['tel']) != 11:
                    print("电话不符合规则，请重新输入")
                    d_student['tel'] = input("请输入手机号:")
                while re.compile(r'^[1-9][0-9]{4,10}@qq\.com').match(d_student['qq'])==None:
                    print("邮箱不符合规则，请重新输入")
                    d_student['qq'] = input("请输入QQ:")
                self.l_student.append(d_student)
                if len(self.l_student) > 1:
                    for i in range(len(self.l_student)-1):
                        if d_student['name'] == self.l_student[i]['name']:
                            self.l_student.remove(d_student)
                            print("此用户名已经被占用,请重新输入")
                            d_student['name'] = input("请输入姓名:")
                            d_student['tel'] = input("请输入手机号:")
                            d_student['qq'] = input("请输入QQ:")
                            d_student['id'] = len(self.l_student)+1
                            self.l_student.append(d_student)
                            L=self.l_student
                        else:
                            L = self.l_student
                else:
                    L = self.l_student
            return L,self.l_student
if __name__ == '__main__':
    S=StudentManmge()
    print(S.add_student())


