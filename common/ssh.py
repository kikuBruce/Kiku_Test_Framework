#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/15
# @Author  : Lin lin

import paramiko
from common.log import log

log = log()


class SSH:
    """
    用于在脚本中对服务器进行操作。

    """

    def __init__(self, host, user, password, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.ssh = None
        self.standard_input = None
        self.standard_out = None
        self.standard_error = None

    def connect(self):
        # ssh通道连接
        if not self.ssh:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                self.ssh.connect(hostname=self.host, port=self.port, username=self.user,
                                 password=self.password, timeout=5)
                log.info("connect to {}".format(self.host))
            except Exception as e:
                log.error(e)
                self.ssh = None
        else:
            pass

    def execute(self, cmd):
        # 执行cmd，返回列表
        self.connect()
        standard_input, standard_out, standard_error = self.ssh.exec_command(cmd, timeout=60)
        self.standard_input = standard_input
        self.standard_out = standard_out
        self.standard_error = standard_error
        return [element[:-1] for element in self.standard_out]

    def connect_trans(self):
        # trans通道
        pass

    def file_upload(self, local_path, remote_path):
        self.connect_trans()
        pass

    def file_download(self, remote_path, local_path):
        self.connect_trans()
        pass


if __name__ == "__main__":
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh = SSH(host='10.9.244.82', user='root', password='V1p3r1@#$%')
    result = ssh.execute('ls')

    for line in result:
        print(line)
