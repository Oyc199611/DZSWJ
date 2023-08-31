# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/26 22:45
"""
import requests
import unittest

from dzswj_autotest_unittest.demo.common.jiaju_util import jiaju_util


class Cms(jiaju_util):

    def test_get_appid(self):
        url = "https://yikeapi.com/account/index"

        res = requests.request(method='get', url=url)
        res = res.text
        print(res)
        # self.assertEqual(res.json()["msg"], "查询用户成功！", msg="testqueryUserList error!")

#
# if __name__ == '__main__':
#     unittest.main()
