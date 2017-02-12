# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.dbConnect import dbConnect
from time import ctime


def count():
    try:
        conn, cur = dbConnect()
        counta = 0
        for i in range(9):
            userTable = "users_" + str(i)
            s = "SELECT uid FROM " + userTable
            cur.execute(s)
            for uid in cur.fetchall():
                counta += 1
        conn.commit()

        print "用户总数为 " + str(counta)
        countb = 0
        for i in range(9):
            userTable = "users_" + str(i)
            s = "SELECT uid FROM " + userTable + " WHERE flag <> 1"
            cur.execute(s)
            for uid in cur.fetchall():
                countb += 1
        print "未读取为 " + str(countb)
        print "已完成用户数为" + str(counta - countb)
        conn.commit()
        print  ctime()
    except MySQLdb.Error as e:
        pass


if __name__ == '__main__':
    count()
