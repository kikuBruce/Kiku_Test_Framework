#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import requests
import unittest
from common.config import Config
from common.log import log

log = log()


class TestBaidu(unittest.TestCase):
    URL = Config().get_config(element='url', index=0)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_baidu(self):
        rsp_code = requests.get(self.URL)
        if rsp_code.status_code == 200:
            log.info('Case Pass')
        else:
            log.error('response code should be 200 ,not be:{}'.format(rsp_code.status_code))


if __name__ == '__main__':
    unittest.main()
