# 统一请求工具类
import requests


# class RequestUtil:
#     # 类变量，通过类名访问
#     session = requests.session()  # cookie = '' # 初始化会话，接口之间可以共享
#     session = requests.session()
#
#     def all_send_request(self, method, url, data, **kwargs):
#         method = str(method).lower()  # 将请求方法转换成小写
#         if method == 'get':  # 如果请求方式是get
#             rep = RequestUtil.session.request(method, url=url, params=data, **kwargs)  # get方法数据用param传参
#         else:  # 如果请求方式是get
#             data = json.dumps(data)  # 不管是表单键值对，还是json，都将其转化成对应的json对象（str)
#             rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)  # post方法数据用data或者json传参
#         return rep.text


class RequestUtil:
    # 类变量，通过类名访问
    session = requests.session()

    def all_send_request(self, **kwargs):
        res = RequestUtil().session.request(**kwargs)  # get方法数据用param传参
        return res
