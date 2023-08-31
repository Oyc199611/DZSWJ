# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/27 0:01
"""
from dzswj_autotest_unittest.common.fixture import Fixture_util


# 将session写入setUpClass的session中
class Login_get_session(Fixture_util):
    def test_login(self):
        self.url = "http://10.199.20.221:38080/login_nsr"
        self.body = {
            "djxh": "10000000333000000118",
            "nsrsbh": "433333333333333477"
        }
        res = self.session.post(self.url, data=self.body)
        print(res.headers)  # 验证调用该类时，只登录了一次


