# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：
测试场景：
1.支付成功
2，支付失败
3，超时，成功
4，超时，失败
5，超时，超时
"""

import unittest
from unittest import mock

from jx_api.jx_tests.API_Mock import payment


class PaymentTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_success(self):
        """
        测试支付成功
        :return:
        """
        pay = payment.Payment()
        # 模拟方法调用的时候不要加圆括号
        pay.requestOutofSystem = mock.Mock(return_value=200)
        resp = pay.doPay(user_id=1, card_num="439019098", amount=200)
        self.assertEqual('success', resp)
        print(pay.requestOutofSystem.assert_called_once())
        print(pay.requestOutofSystem.assert_called_once_with("439019098",200))

    def test_fail(self):
        """
        测试支付失败
        :return:
        """
        pay = payment.Payment()
        # 模拟方法调用的时候不要加圆括号
        pay.requestOutofSystem = mock.Mock(return_value=500)
        resp = pay.doPay(user_id=2, card_num="439019908", amount=20000)
        self.assertEqual('fail', resp)

    def test_timemout_success(self):
        """
        测试支付超时,成功
        :return:
        """
        pay = payment.Payment()
        # 模拟方法调用的时候不要加圆括号
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])
        print("是否被调用", pay.requestOutofSystem.called)
        resp = pay.doPay(user_id=2, card_num="439019908", amount=20000)
        print("是否被调用", pay.requestOutofSystem.called)
        print("调用次数", pay.requestOutofSystem.call_count)
        print("调用参数", pay.requestOutofSystem.call_args)

        self.assertEqual('success', resp)

    def test_timemout_fail(self):
        """
        测试支付超时,失败
        :return:
        """
        pay = payment.Payment()
        # 模拟方法调用的时候不要加圆括号
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = pay.doPay(user_id=2, card_num="439019908", amount=20000)
        self.assertEqual('fail', resp)

    def test_timemout(self):
        """
        测试支付超时,超时
        :return:
        """
        try:
            pay = payment.Payment()
            # 模拟方法调用的时候不要加圆括号
            pay.requestOutofSystem = mock.Mock(side_effect=TimeoutError)
            resp = pay.doPay(user_id=2, card_num="439019908", amount=20000)
        except TimeoutError as e:
            self.assertTrue(e)

    def tearDown(self):
        pass
