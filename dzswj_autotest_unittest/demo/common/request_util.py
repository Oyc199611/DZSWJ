# ͳһ���󹤾���
import requests


# class RequestUtil:
#     # �������ͨ����������
#     session = requests.session()  # cookie = '' # ��ʼ���Ự���ӿ�֮����Թ���
#     session = requests.session()
#
#     def all_send_request(self, method, url, data, **kwargs):
#         method = str(method).lower()  # �����󷽷�ת����Сд
#         if method == 'get':  # �������ʽ��get
#             rep = RequestUtil.session.request(method, url=url, params=data, **kwargs)  # get����������param����
#         else:  # �������ʽ��get
#             data = json.dumps(data)  # �����Ǳ���ֵ�ԣ�����json��������ת���ɶ�Ӧ��json����str)
#             rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)  # post����������data����json����
#         return rep.text


class RequestUtil:
    # �������ͨ����������
    session = requests.session()

    def all_send_request(self, **kwargs):
        res = RequestUtil().session.request(**kwargs)  # get����������param����
        return res
