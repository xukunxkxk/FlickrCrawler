# __author__=xk
# -*- coding: utf-8 -*-
# 用于创建数据库

import MySQLdb


def dbCreate():
    try:
        conn = MySQLdb.connect('localhost', 'dyn', '123')
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS test")
        print "Database Create Successfully"
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print e


if __name__ == '__main__':
    dbCreate()
