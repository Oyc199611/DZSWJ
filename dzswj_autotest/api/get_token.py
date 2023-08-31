# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/24 11:23
"""
from dzswj_autotest.common.request_util import RequestUtil

"""
Code description：获取token
"""
import os
import urllib3


class Get_Token(object):

    def get_token(self, djxh='****', nsrsbh='****'):
        # url = "http://192.168.2.199:9092/v1/auth/developer/accountLogin"
        # url = os.environ["host"] + "/v1/auth/developer/accountLogin"
        url = "http://10.199.20.221:38080/login_nsr"
        body = {
            "djxh": "10000000333000000118",
            "nsrsbh": "433333333333333477"
        }
        # 代表屏蔽全部warning类型
        urllib3.disable_warnings()
        # verify=False是指请求时不验证SSL证书的有效性
        req = RequestUtil().all_send_request(method='post', url=url, data=body, verify=False)
        # cookie = req.headers['Set-Cookie']
        return req

    # def get_header(self):
    #     cookie = Get_Token.get_token(self)
    #     url = 'http://10.199.20.221:8081/wszx-web/api/person/getZlxgTzs'
    #     req = RequestUtil().all_send_request(method='get', url=url, verify=False)
    #     print(req.json())

#     def test_get_token(self):
#         Get_Token().get_token()
#         url = 'http://10.199.20.221:8081/yhs-web/api/bsjd/query/list'
#         data = {"rqq": "2023-05-04", "rqz": "2023-08-25", "bsjd": "", "rwmc": "", "bsjdlx": "", "kqhDjxh": "",
#                 "sfsbDm": "", "fromtc": ""}
#         req = RequestUtil().all_send_request(method='post', url=url, json=data, verify=False)
#         print(req.json())
#         print(req.headers)
#
#
# if __name__ == '__main__':
#     Get_Token().test_get_token()
