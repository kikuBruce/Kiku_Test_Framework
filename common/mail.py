#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/21
# @Author  : Lin lin

import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg_from = ''
password = ''
msg_to = []

subject = 'mail taitle'
content = 'mail content'

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
