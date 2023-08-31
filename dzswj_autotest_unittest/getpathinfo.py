# -*- coding:utf-8 -*-
"""
@Author : oyc
@Time : 2023/8/24 13:36
"""
"""
Code description:配置文件路径
"""
import os


def get_path():
    # 获取当前项目根路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    return curpath

