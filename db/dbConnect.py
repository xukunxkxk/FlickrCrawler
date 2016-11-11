# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
def dbConnect():
    try:
        conn = MySQLdb.connect('localhost', 'dyn', '123','test')
        cur = conn.cursor()
        print "Database Connected Successfully"
        return (conn,cur)
    except MySQLdb.Error as e:
        print e
        return (None,None)

if __name__ == '__main__':
    dbConnect()