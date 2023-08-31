# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/8/29 19:18
"""

import random
import time


class DebugTalk:

    # 获得随机数
    def get_randon_number(self, min, max):
        return random.randint(int(min), int(max))

    # 读取extract.yaml文件中的值
    # def read_extract_data(self, key):
    #     return YamlUtil().read_yaml(key)
