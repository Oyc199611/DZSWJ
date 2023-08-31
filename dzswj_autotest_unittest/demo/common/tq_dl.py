# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/26 23:35
"""
from dzswj_autotest_unittest.demo.common.jiaju_util import jiaju_util


class Login(jiaju_util):

    def testlogin(self):
        self.url = "https://tianqiapi.com/user/login"
        self.body = {
            "username": "13767594293@163.com",
            "password": "ouyangchao199611",
            "registerSubmit": ""
        }
        # 通过全局 session 请求接口
        # res = self.session.post(self.url, data=self.body)
        res = self.session.post(self.url, data=self.body)
        print(res.json())
