# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.dbConnect import dbConnect


def alterTable():
    conn, cur = dbConnect()
    for i in range(0, 9):
        try:
            tableName = "photos_" + str(i)
            sql = "alter table " + tableName + " modify column tags varchar(800)"
            print sql
            cur.execute(sql)
        except MySQLdb.Error as e:
            print e




if __name__ == '__main__':
    alterTable()
