# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from dbConnect import dbConnect
from time import ctime


def mergeTable():
    try:
        conn, cur = dbConnect()
        userTab = []
        print ctime()
        try:
            for i in range(9):
                userTable = "users_" + str(i)
                s = "SELECT uid,flag FROM " + userTable
                cur.execute(s)
                for uid in cur.fetchall():
                    userTab.append((uid[0], uid[1]))  # 返回的是一个元组，取第一个
            print len(userTab)
        except MySQLdb.Error as e:
            print e
        conn.commit()
        print ctime()
        j = 0
        a = ctime()
        for i in userTab:
            try:
                j += 1
                cur.execute("INSERT INTO user(uid,flag) VALUES(%s,%s)", (i[0], i[1]))
                print i[0]
                if j % 500 == 0:
                    conn.commit()
            except MySQLdb.Error as e:
                print e
        conn.commit()
        print a
        print ctime()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print e


if __name__ == '__main__':
    mergeTable()
