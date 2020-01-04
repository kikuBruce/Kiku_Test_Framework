#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin

import yaml
import os


class YamlReader:
    """用于接收yaml_file，data方法作为属性的形式判断是否首次调用并返回self._data

    """

    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_f = yaml_file
        else:
            raise FileNotFoundError("yaml文件不存在")
        self._data = None

    @property
    def data(self):
        # 第一次调用读取yml转换成list, 否则用原有_data
        if not self._data:
            with open(self.yaml_f, 'r') as f:
                self._data = list(list(yaml.safe_load_all(f)))
            return self._data
