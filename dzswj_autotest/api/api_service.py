# -*- coding:utf-8 -*-
"""
@Author : oyc
@Time : 2023/8/24 11:22
"""
import json

from dzswj_autotest.common.request_util import RequestUtil

"""
Code description:服务相关接口
"""

import os


class Api_Auth_Service:

    # def __init__(self):
    #     self.headers = RequestUtil().headers

    # 办税进度查询结果
    def api_getBsjdResult(self, body):
        # 读取conftest.py文件地址进行拼接
        body = body
        # print(body)
        url = os.environ["host"] + "/yhs-web/api/bsjd/query/list"
        response = RequestUtil().all_send_request(method='post', url=url, json=body, verify=False)
        # print(response.headers)
        return response.text

    def api_subGzsb(self, body):
        # 读取conftest.py文件地址进行拼接
        body = body
        # print(body)
        url = os.environ["host"] + "/nfzx-web/api/sbcwgz/submit"
        response = RequestUtil().all_send_request(method='post', url=url, json=body, verify=False)
        return response.text
