#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/15
# @Author  : Lin lin

import paramiko
from common.log import log

log = log()


class SSH:
    def __init__(self, host, user, password, port=22):
        self.ip = host
        self.user = user
        self.password = password
        self.ssh = None
        self.port = port

    def connect(self):
        # ssh通道连接
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(hostname=self.ip, port=self.port, username=self.user, password=self.password, timeout=1)
        except Exception as e:
            log.error(e)
            self.ssh = None

    def exce(self, cmd):
        # 执行cmd
        self.connect()
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        self.stdin = stdin
        self.stderr = stderr
        self.stdout = stdout
        return [element[:-1] for element in self.stdout]
        self.ssh.close()

    def connect_trans(self):
        # trans通道
        pass

    def file_upload(self, local_path, remote_path):
        pass

    def file_download(self, remote_path, local_path):
        pass


if __name__ == "__main__":
    ssh = SSH(host='192.168.123.62', user='pi', password='raspberry')
    result = ssh.exce(r"ls -l | awk '{print $9}'")
    for line in result:
        print(line)