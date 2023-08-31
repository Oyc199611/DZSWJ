# -*- coding:utf-8 -*-
import unittest
from ddt import data, ddt, unpack


from dzswj_autotest_unittest.demo.case.test import Cms

# # 用的少
# def setUpModule():
#     print("模块级别开始的夹具")
#
#
# def tearDownModule():
#     print("模块级别结束的夹具")




if __name__ == '__main__':
    # unittest_test.main()
    # print('test')

    # 测试套件，一个一个加
    suite = unittest.TestSuite()
    suite.addTest(Cms("test_get_appid"))
    # suite.addTest(Test_Ddt("test_test01"))
    # unittest.main(defaultTest='suite')  # 执行方式1
    unittest.TextTestRunner().run(suite)  # 执行方式2
