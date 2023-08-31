# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/26 11:35
"""
import os
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 测试套件，一个一个加
    # suite = unittest.TestSuite()
    # suite.addTest(Test_unittest.Test_Ddt("test01_get"))
    # suite.addTest(Test_unittest.Test_Ddt("test02_post"))
    # unittest.main(defaultTest='suite')  # 执行方式1
    # unittest.TextTestRunner().run(suite)  # 执行方式2

    # 一次加载所有的用例
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir=os.path.dirname(os.path.abspath(__file__)) + '/case',
                                                    pattern='*.py')
    suite.addTests(testcases)
    # # unittest.main(defaultTest='suite')  # 执行方式1
    # unittest.TextTestRunner().run(suite)  # 执行方式2

    # 生成报告
    fatherpath = os.path.dirname(os.path.abspath(__file__))
    current_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    report_path = fatherpath + '/report'
    print(report_path)
    fp = open(report_path+"/"+current_time+"_report.html", "wb")
    # 需要下载HTMLTestRunner.py 放到python/lib目录下
    runner = HTMLTestRunner(stream=fp, title="接口自动化测试报告", description='报告详情如下')
    runner.run(suite)
