#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/1/6
# @Author  : Lin lin


import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.config import Config, LOG_PATH


def log(logger_name=None, c_level=None, f_level=None, f_name=None, f_path=None):
    """封装logging，默认when为D（天单位）10个file为上限，控制台日志级别为debug以上，file为info以上

    :param logger_name:
    :param c_level:
    :param f_level:
    :param f_name:
    :param f_path:
    :return:
    """
    get_elm_by_config = Config().get_config(element='log')
    print()

    log_path = LOG_PATH if f_path is None else f_path
    f_name = os.path.join(log_path, get_elm_by_config.get('file_name')) if f_name is None else os.path.join(log_path, f_name)
    logger = logging.getLogger(get_elm_by_config.get('file_name')) if logger_name is None else logging.getLogger(logger_name)

    formatter = logging.Formatter(get_elm_by_config.get('pattern'))

    logger.setLevel(get_elm_by_config.get('console_level'))

    c_handler = logging.StreamHandler()
    c_handler.setLevel(get_elm_by_config.get('console_level')) if c_level is None else c_handler.setLevel(c_level)
    c_handler.setFormatter(formatter)

    f_handler = TimedRotatingFileHandler(f_name, when='D', interval=1, backupCount=get_elm_by_config.get('backup'), encoding='utf-8')
    f_handler.setLevel(get_elm_by_config.get('file_level')) if f_level is None else f_handler.setLevel(f_level)
    f_handler.setFormatter(formatter)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


if __name__ == "__main__":
    log = log()
    log.debug('debug msg...')
    log.info('info msg...')
    log.error('error msg...')
    log.critical('critical msg...')
