#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/4
# @Author  : Lin lin


import requests
import unittest
from common.config import Config


class TestBaidu(unittest.TestCase):
    URL = Config().get_config(element='url', index=0)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_baidu(self):
        rsp_code = requests.get(self.URL)
        self.assertEqual(rsp_code, 200)


if __name__ == '__main__':
    unittest.main()
