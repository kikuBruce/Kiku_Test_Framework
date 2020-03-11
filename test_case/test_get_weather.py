#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import requests
import unittest
import json
from common.config import Config, DATA_PATH
from common.log import log
from common.file_reader import ExcelReader
from common import HTMLTestRunner

log = log()


class TestGetWeather(unittest.TestCase):
    excel_data = ExcelReader(excel_file=os.path.join(DATA_PATH, 'CityCode.XLS'), title=True, sheet=0).data

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_weather_by_shenzhen(self):
        city_name = "深圳"
        log.info("获取城市编码...")
        for index in range(0, len(self.excel_data)):
            if self.excel_data[index].get('ChinsesName') == city_name:
                city_code = self.excel_data[index].get('CityCode')
                log.info("城市名称：{0}； CityCode: {1}".format(city_name, city_code))
                break

        _url = Config().get_config(element='url', index=0) + '?' + 'id={}'.format(city_code)
        rsp = requests.get(url=_url)
        self.assertEqual(rsp.status_code, 200)

    def test_get_weather_by_default_citycode(self):
        _url = Config().get_config(element='url', index=0)
        log.info(_url)
        rsp = requests.get(url=_url)
        self.assertEqual(rsp.json().get('city'), '长春')


if __name__ == '__main__':
    unittest.main()
