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


class Api_Auth_Service(object):

    # def __init__(self):
    #     self.headers = RequestUtil().headers

    # 办税进度查询结果
    def api_getBsjdResult(self, body):
        # 读取conftest.py文件地址进行拼接
        body = body
        print(body)
        url = os.environ["host"] + "/yhs-web/api/bsjd/query/list"
        response = RequestUtil().all_send_request(method='post', url=url, json=body, verify=False)
        # print(response.headers)
        response = response.json()
        return response

    # def api_home_service_list(self):
    #     # 首页服务列表
    #     url = "http://192.168.2.199:9092/v1/auth/auth_service/findAuthService"
    #     # url = os.environ["host"] + "/v1/auth/auth_service/findAuthService"  # 读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='post', url=url, headers=self.headers, verify=False)
    #     # print(response.json())
    #     return response
    #
    # def get_service_id(self):
    #     # 获取银行卡三要素认证服务id
    #     url = "http://192.168.2.199:9092/v1/auth/auth_service/findAuthService"
    #     # url = os.environ["host"] + "/v1/auth/auth_service/findAuthService"  # 读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='get',url=url, headers=self.headers)
    #     # print(response.json()['data'][0]['service_list'][0]['id'])
    #     service_id = response.json()['data'][0]['service_list'][1]['id']
    #     return service_id
    #
    # def api_service_info(self, serviceId='', developerId=''):
    #     # 服务详情
    #     body = {
    #         "serviceId": serviceId,
    #         "developerId": developerId
    #     }
    #     url = "http://192.168.2.199:9092/v1/auth/auth_service/findServiceDetail"
    #     # url = os.environ["host"] + "/v1/auth/auth_service/findServiceDetail"#读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='get', url=url, headers=self.headers, params=body, verify=False)
    #     # print(response.json())
    #     return response
    #
    # def api_add_or_update_service(self, api_param_req, api_param_res, description, error_code, icon, id,
    #                               interface_remarks,
    #                               name, product_info, request_method, sample_code, sort, type, url):
    #     # 服务添加或者更新
    #     body = {
    #         "api_param_req": api_param_req,
    #         "api_param_res": api_param_res,
    #         "description": description,
    #         "error_code": error_code,
    #         "icon": icon,
    #         "id": id,
    #         "interface_remarks": interface_remarks,
    #         "name": name,
    #         "product_info": product_info,
    #         "request_method": request_method,
    #         "sample_code": sample_code,
    #         "sort": sort,
    #         "type": type,
    #         "url": url,
    #     }
    #     # url = "http://192.168.2.199:9092/v1/auth/auth_service/insertOrUpdateService"
    #     url = os.environ["host"] + "/v1/auth/auth_service/insertOrUpdateService"  # 读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='post', url=url, json=body, headers=self.headers, verify=False)
    #     return response
    #
    # def api_add_service_price(self, id, max_number, money, service_id, small_number):
    #     # 服务价格添加
    #     body = {
    #         "id": id,
    #         "max_number": max_number,
    #         "money": money,
    #         "service_id": service_id,
    #         "small_number": small_number
    #     }
    #     # url = "http://192.168.2.199:9092/v1/auth/auth_service/insertServicePrice"
    #     url = os.environ["host"] + "/v1/auth/auth_service/insertServicePrice"  # 读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='post', url=url, json=body, headers=self.headers, verify=False)
    #     return response
    #
    # def api_apply_service(self, developer_id, service_id):
    #     # 申请服务
    #     body = {
    #         "developer_id": developer_id,
    #         "service_id": service_id
    #     }
    #     # url = "http://192.168.2.199:9092/v1/auth/auth_service/applyService"
    #     url = os.environ["host"] + "/v1/auth/auth_service/applyService"  # 读取conftest.py文件地址进行拼接
    #     response = RequestUtil().all_send_request(method='post', url=url, json=body, headers=self.headers, verify=False)
    #     return response

# if __name__ == '__main__':
#     Auth_Service().api_home_service_list()
#     print(Api_Auth_Service().api_getBsjdResult())
#     Auth_Service().api_service_info()
