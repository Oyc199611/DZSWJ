# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/26 13:05
"""
import unittest

import requests


class jiaju_util(unittest.TestCase):

    @classmethod  # 作用于类
    def setUpClass(cls) -> None:
        cls.session = requests.Session()  # 通过 session 保持会话
        print("... Start test ...")

    def setUp(self):
        print("setUp打开浏览器")

    def tearDown(self):
        print("tearDown关闭浏览器")

    @classmethod  # 作用于类
    def tearDownClass(cls) -> None:
        print('执行用例后关闭数据库或者生成日志对象')
