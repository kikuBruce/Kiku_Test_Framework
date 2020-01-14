#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import requests
import unittest
import os
import json
from common.config import Config, DATA_PATH
from common.log import log
from common.file_reader import ExcelReader

log = log()


class TestGetWeather(unittest.TestCase):
    excel_file = os.path.join(DATA_PATH, 'CityCode.XLS')
    excel_data = ExcelReader(excel_file=excel_file, title=True, sheet=0).data

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_weather_by_shenzhen(self):
        city_name = "深圳"
        log.info('*' * 20 + "获取城市编码" + '*' * 20)
        for index in range(0, len(self.excel_data)):
            if self.excel_data[index].get('ChinsesName') == city_name:
                city_code = self.excel_data[index].get('CityCode')
                log.info("获取城市编码成功，城市名称：{0}； CityCode: {1}".format(city_name, city_code))
                break

        _url = Config().get_config(element='url', index=0) + '?' + 'id={}'.format(city_code)
        rsp = requests.get(url=_url)
        self.assertEqual(rsp.status_code, 200)
        dict_rsp = json.loads(rsp.text)
        log.info("{0} {1} \
        \t 温度: {2} \
        \t 天气：{3} \
        \t pm2.5：{4}".format(city_name, dict_rsp.get('today'),
                             dict_rsp.get('city'),
                             dict_rsp.get('temp'),
                             dict_rsp.get('weather'),
                             dict_rsp.get('pm25')
                             ))

    if __name__ == '__main__':
        unittest.main()
