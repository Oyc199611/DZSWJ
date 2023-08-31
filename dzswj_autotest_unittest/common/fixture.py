# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/26 13:05
"""
import unittest

import requests


class Fixture_util(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()  # 通过 session 保持会话
        print("... Start test ...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("... End test ...")

    def setUp(self):
        print("... 开始登录 ...")

    def tearDown(self):
        print("... 登录结束 ...")
