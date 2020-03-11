#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import os
from common.file_reader import YamlReader

__all__ = ['Config', 'BASE_PATH', 'CONFIG_PATH', 'DATA_PATH', 'DRIVER_PATH', 'LOG_PATH', 'REPORT_PATH', 'TEST_CASE_PATH']

# 当前file的目录上层目录的路径作为项目基础路径
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# 一些目录的path定义为常量
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_CASE_PATH = os.path.join(BASE_PATH, 'test_case')

# 一些file定义为常量
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')


class Config:
    """用于获取config目录下的config.yml，从中获取key对应的value。

    """

    def __init__(self, config_file=CONFIG_FILE):
        self.config = YamlReader(config_file).data

    def get_config(self, element, index=0):
        """
        :param element: yaml种的的key
        :param index: yaml中以'---'作为分割，默认取index=0
        :return: config[index].element

        """
        return self.config[index].get(element)
