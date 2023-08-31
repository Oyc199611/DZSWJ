# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/24 20:42
"""
import json
import os
import sys
import unittest
from turtle import pd

from ddt import data, ddt, unpack, file_data

from dzswj_autotest_unittest import getpathinfo
from dzswj_autotest_unittest.api.api_service import Api_Auth_Service
from dzswj_autotest_unittest.common.logger import Log
from dzswj_autotest_unittest.common.yml_util import YamlUtil


@ddt  # 数据驱动测试
class Test_Service_Info(unittest.TestCase):
    log = Log()
    path = getpathinfo.get_path()  # 获取项目根路径
    testdata = YamlUtil().read_testcase_yaml("./data/test_data/api_GetBsjd_data.yml")  # 读取数据

    @data(*testdata)  # 字典列表解析成list
    # data = path + "./data/test_data/api_GetBsjd_data.yml"
    # @file_data(data)  # 字典列表解析成list,使用他会有编码错误，哎
    @unpack
    def test01_BsjdQuery(self, name, datas, validate):
        print(name)
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % datas))
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
        msg = Api_Auth_Service().api_getBsjdResult(datas)
        msg = json.loads(msg)
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % msg))
        # 断言
        if msg["success"] == True and len(msg["value"]) != 0:
            assert msg["success"] == validate
            # value格式：
            # value = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # a = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # for i in a:
            #     print(i['a'])
            YamlUtil().clear_yaml(Test_Service_Info().path + '/data/save_data/api_GetBsjd_details.yml')
            for i in msg["value"]:
                # print(i['sqxq'])
                YamlUtil().write_yaml(Test_Service_Info().path + '/data/save_data/api_GetBsjd_details.yml', i['sqxq'])
        if msg["success"] == False:
            assert msg["message"] == validate

    # @data(*testdata)
    # @unpack
    # def test011_BsjdQuery(self, name, datas, validate):
    #     name = name
    #     datas = datas
    #     validate = validate
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % datas))
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
    #     msg = Api_Auth_Service().api_getBsjdResult1(datas)
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % msg))
    #     # 断言
    #     if msg["success"] == True and len(msg["value"]) != 0:
    #         assert msg["success"] == validate
    #         # value格式：
    #         # value = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
    #         # a = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
    #         # for i in a:
    #         #     print(i['a'])
    #         YamlUtil().clear_yaml(Test_Service_Info().path + '/data/save_data/api_GetBsjd_details.yml')
    #         for i in msg["value"]:
    #             # print(i['sqxq'])
    #             YamlUtil().write_yaml(Test_Service_Info().path + '/data/save_data/api_GetBsjd_details.yml', i['sqxq'])
    #     if msg["success"] == False:
    #         assert msg["message"] == validate

    # def test_Bsjd_details(self, caseinfo):
    #     data = caseinfo['data']
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % data))
    #     name = caseinfo['name']
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
    #     msg = Api_Auth_Service().api_getBsjdResult(data)
    #     self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % msg))
    #     # 断言
    #     if msg["success"] == True:
    #         assert msg["success"] == caseinfo['validate']
    #     else:
    #         assert msg["message"] == caseinfo['validate']
