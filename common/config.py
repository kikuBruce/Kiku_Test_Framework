#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import os
from common.file_reader import YamlReader

__all__ = ['Config']

# path
# 取当前file的目录名分割后取file上层目录的路径作为项目基础路径
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_CASE_PATH = os.path.join(BASE_PATH, 'test_case')

# file
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get_config(self, element, index=0):
        """
        :param element:
        :param index: yaml中以'---'作为分割，默认取index=0
        :return: config[index].element

        """
        return self.config[index].get(element)
