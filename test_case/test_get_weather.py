#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import os
import sys
import requests
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from common.config import Config, DATA_PATH, REPORT_PATH
from common.log import log
from common.file_reader import ExcelReader
from common.HTMLTestRunner import HTMLTestRunner


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

    def test_get_weather_by_default(self):
        _url = Config().get_config(element='url', index=0)
        log.info(_url)
        rsp = requests.get(url=_url)
        self.assertEqual(rsp.json().get('city'), '长春')


if __name__ == '__main__':
    # unittest.main()
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='TestGetWeather', description='TestGetWeather')
        runner.run(TestGetWeather('test_get_weather_by_shenzhen'))