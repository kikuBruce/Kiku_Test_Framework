#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/6
# @Author  : Lin lin


import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.config import Config, LOG_PATH


def log_config(logger_name=None, c_level=None, f_level=None, f_name=None, f_path=None):
    log_path = LOG_PATH if f_path is None else f_path
    f_name = os.path.join(log_path, 'test_log_file') if f_name is None else os.path.join(log_path, f_name)
    logger = logging.getLogger('file_name') if logger_name is None else logging.getLogger(logger_name)

    formatter = logging.Formatter(
        '[%(levelname)s][%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')

    logger.setLevel(logging.DEBUG)

    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG) if c_level is None else c_handler.setLevel(c_level)
    c_handler.setFormatter(formatter)

    f_handler = TimedRotatingFileHandler(f_name + '.log', when='S', backupCount=10)
    f_handler.setLevel(logging.INFO) if f_level is None else f_handler.setLevel(f_level)
    f_handler.setFormatter(formatter)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


if __name__ == "__main__":
    log = log_config()
    log.debug('debug msg...')
    log.info('info msg...')
    log.error('error msg...')
    log.critical('critical msg...')
