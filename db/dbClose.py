# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb


def dbClose(conn, cur):
    try:
        cur.close()
        conn.close()
        print "Databese Disconnected successfully"
    except MySQLdb.Error as e:
        print e


if __name__ == '__main__':
    pass
