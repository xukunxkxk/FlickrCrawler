# __author__=xk
# -*- coding: utf-8 -*-
from dbConnect import dbConnect
import MySQLdb


def correctWrongUpdate():
    wrongFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\wrong', 'r')
    wrongUid = []
    for line in wrongFile.readlines():
        wrongUid.append(line.strip())
    try:
        conn, cur = dbConnect()
        count = 0
        for uid in wrongUid:
            count += 1
            cur.execute("UPDATE user SET flag=0 WHERE uid=%s", (uid,))
            print "uid %s has been correct" % uid
            if count % 500 == 0:
                conn.commit()
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print e
        exit()
    wrongFile.close()


def correctWrongUpdateByUidRange(uidLowBound, uidHighBOund):
    try:
        conn, cur = dbConnect()
        s = "UPDATE users_2 SET flag=0 WHERE uid BETWEEN %s AND %s" % (uidLowBound, uidHighBOund)
        print s
        cur.execute(s)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print e
        exit()


def findMinUid():
    try:
        conn, cur = dbConnect()
        uid = []
        cur.execute("SELECT uid FROM userfollowers ORDER BY id DESC LIMIT 0, 50000")
        for uids in cur.fetchall():
            uid.append(uids[0])
        print len(uid)
        print max(uid)
    except MySQLdb.Error as e:
        print e
        exit()


if __name__ == '__main__':
    # correctWrongUpdate()
    # findMinUid()
    correctWrongUpdateByUidRange('43119868@N02', '51313069@N02')
