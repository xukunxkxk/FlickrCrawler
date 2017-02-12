# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.dbConnect import dbConnect


def group(uid):
    return uid[len(uid) - 1]


def test():
    try:
        conn, cur = dbConnect()
        try:
            sum = 0
            for i in range(9):
                cur.execute("SELECT COUNT(*) FROM users_" + str(i))
                sum += cur.fetchone()[0]
            print sum
        except MySQLdb.Error as e:
            print e
        try:
            sum = 0
            for i in range(9):
                cur.execute("SELECT COUNT(*) FROM users_" + str(i) + " WHERE flag<>1")
                sum += cur.fetchone()[0]
            print sum
        except MySQLdb.Error as e:
            print e

    except MySQLdb.Error as e:
        print e


if __name__ == '__main__':
    test()
