# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from tools.hostname import hostname

def dbConnect():
    try:
        if hostname() == "DESKTOP-S1OH3KQ":
            host = "localhost"
        else:
            host = "223.3.93.40"
        print "Trying to connect %s" % host
        conn = MySQLdb.connect(host, 'dyn', '123', 'test')
        cur = conn.cursor()
        print "Database Connected Successfully"
        return (conn, cur)
    except MySQLdb.Error as e:
        print e
        return (None, None)


if __name__ == '__main__':
    conn, cur = dbConnect()
    cur.close()
    conn.close()


