#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin

import yaml
from xlrd import open_workbook
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


class ExcelReader:
    """用于读取Excel,提供返回带title的键值对列表和不含title的列表

    """

    def __init__(self, excel_file, sheet=0, title=True):
        if os.path.exists(excel_file):
            self.excel_f = excel_file
        else:
            raise FileNotFoundError("excel文件不存在")

        self.sheet = sheet
        self.title = title
        self._data = list()

    @property
    def data(self):
        # 首次调用
        if not self._data:
            workbook = open_workbook(self.excel_f)
            # 根据index类型返回操作句柄
            if isinstance(self.sheet, int):
                sheet = workbook.sheet_by_index(sheetx=self.sheet)
            elif isinstance(self.sheet, str):
                sheet = workbook.sheet_by_name(sheet_name=self.sheet)
            else:
                raise TypeError("sheet 参数应该是int或者str类型，而不是{}".format(type(self.sheet)))

            # 根据tittle的布尔值返回
            # 如果为真，把可迭代的titles和values组合为键值对，每一行作为字典追加到列表，否则直接追加到列表
            if self.title:
                titles = sheet.row_values(rowx=0)
                for col in range(1, sheet.nrows):
                    values = sheet.row_values(rowx=col)
                    _dict = dict(zip(titles, values))
                    self._data.append(_dict)
            else:
                for col in range(1, sheet.nrows):
                    values = sheet.row_values(rowx=col)
                    self._data.append(values)

        return self._data


if __name__ == '__main__':
    from common.config import DATA_PATH

    excel_file = os.path.join(DATA_PATH, 'CityCode.XLS')
    excel_reader = ExcelReader(excel_file=excel_file, sheet=0, title=True)
    print(excel_reader.data)

    for i in excel_reader.data:
        if i['ReadmeName'] is not '':
            print(i['ReadmeName'])
        else:
            continue
