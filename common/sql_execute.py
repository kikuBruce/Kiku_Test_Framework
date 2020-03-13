#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/3/13
# @Author  : Lin lin

import cx_Oracle


class Oracle_Execute:

    def __init__(self, user, password, db, encoding="UTF-8", dsn=None):
        self.user = user
        self.password = password
        if ":" in db:
            self.db = db
        else:
            self.host = db.split('/')[0]
            self.uri = db.split('/')[1]
            self.db = "{0}:{1}".format(self.host, self.uri)
            self.encoding = encoding
            self.dsn = dsn

        self._connection = cx_Oracle.connect(user=self.user, password=self.password,
                                             dsn=self.dsn, encoding=self.encoding)
        self.cursor = self._connection.cursor()

    def close_connection(self):
        self._connection.close()

    def commit(self):
        self._connection.commit()

    def query_all(self, sql):
        if sql[:-1] == ';' or sql[:-1] == '/':
            raise ValueError('Oracle的语句尾部不应包含";"或者"/"')
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except Exception:
            raise ValueError("sql执行异常，请检查sql语句：{}".format(sql))
        finally:
            self.close_connection()

        result_list = []
        for row in rows:
            result_list.append(row)

        return result_list

    def insert_in_to(self, data={}):
        if not data:
            raise ValueError("data不能为空")
        pass
        self.close_connection()


if __name__ == "__main__":
    orc = Oracle_Execute(user="test", password="test", host="172.20.25.16:")
    print(orc.query_all())
