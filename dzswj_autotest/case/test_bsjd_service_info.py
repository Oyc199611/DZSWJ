# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/24 20:42
"""
import sys
import allure
import pytest

from dzswj_autotest.api.api_service import Api_Auth_Service
from dzswj_autotest.common.logger import Log
from dzswj_autotest.common.yml_util import YamlUtil


class Test_Service_Info(object):
    log = Log()
    testdata = YamlUtil().read_testcase_yaml("./data/test_data/api_GetBsjd_data.yml")  # 读取数据

    @allure.step('办税进度查询')
    @pytest.mark.parametrize('caseinfo', testdata)
    def test_BsjdQuery(self, caseinfo):
        data = caseinfo['data']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % data))
        name = caseinfo['name']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
        msg = Api_Auth_Service().api_getBsjdResult(data)
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % msg))
        # 断言
        if msg["success"] == True and len(msg["value"]) != 0:
            assert msg["success"] == caseinfo['validate']
            # value格式：
            # value = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # a = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # for i in a:
            #     print(i['a'])
            YamlUtil().clear_yaml('./data/save_data/api_GetBsjd_details.yml')
            for i in msg["value"]:
                # print(i['sqxq'])
                YamlUtil().write_yaml('./data/save_data/api_GetBsjd_details.yml', i['sqxq'])
        if msg["success"] == False:
            assert msg["message"] == caseinfo['validate']

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
