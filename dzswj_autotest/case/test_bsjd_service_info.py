# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/24 20:42
"""
import json
import sys
import allure
import pytest

from dzswj_autotest.api.api_service import Api_Auth_Service
from dzswj_autotest.common.connect_oracle import select_sql, execute_sql
from dzswj_autotest.common.logger import Log
from dzswj_autotest.common.yml_util import YamlUtil


class Test_Service_Info(object):
    log = Log()
    bsjd_testdata = YamlUtil().read_testcase_yaml("./data/test_data/api_GetBsjd_data.yml")  # 读取数据
    gzsb_testdata = YamlUtil().read_testcase_yaml("./data/test_data/api_SubGzsb_data.yml")  #

    @allure.step('办税进度查询')
    @pytest.mark.parametrize('caseinfo', bsjd_testdata)
    def test_BsjdQuery(self, caseinfo):
        data = caseinfo['data']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % data))
        name = caseinfo['name']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
        data = Api_Auth_Service().api_getBsjdResult(data)
        data = json.loads(data)
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % data))
        # 断言
        if data["success"] == True and len(data["value"]) != 0:
            assert data["success"] == caseinfo['validate']
            # value格式：
            # value = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # a = [{'a': '1'}, {'a': '2'}, {'a': '3'}]
            # for i in a:
            #     print(i['a'])
            YamlUtil().clear_yaml('./data/save_data/api_GetBsjd_details.yml')
            for i in data["value"]:
                # print(i['sqxq'])
                YamlUtil().write_yaml('./data/save_data/api_GetBsjd_details.yml', i['sqxq'])
        if data["success"] == False:
            assert data["message"] == caseinfo['validate']

    @allure.step('更正申报提交')
    @pytest.mark.parametrize('caseinfo', gzsb_testdata)
    def test_gzsb_submit(self, caseinfo):
        data = caseinfo['data']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------获取请求参数：------%s' % data))
        name = caseinfo['name']
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '------用例场景：------%s' % name))
        data = Api_Auth_Service().api_subGzsb(data)
        data = json.loads(data)
        self.log.info('%s:%s' % (sys._getframe().f_code.co_name, '获取请求结果：%s' % data))
        # 断言
        if data["success"] == True and len(data["value"]) != 0:
            assert data["success"] == caseinfo['validate']
            sqxh = data["value"]["sqxh"]
            sql = "delete  ws_sqqk where sqxh ="+"'"+sqxh+"'"
            execute_sql(sql, 'wtwscl', 'wtwscl')
        else:
            assert data["success"] == False
