# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from dbConnect import dbConnect
from threading import Thread
def group(uid):
    pos=len(uid)-5
    return uid[pos-2]+uid[pos-1]+uid[pos]

def tablesId(i):
    if i>=0 and i<=9:
        return "00"+str(i)
    elif i>=10 and i<=99:
        return "0"+str(i)
    else:
        return str(i)

def insertTableThread(data,conn,cur,tableId):
    for i in data:
        try:
            s = "INSERT INTO users_" + tableId + "(uid,flag) VALUES(%s,%s)"
            cur.execute(s, (i[0], i[1]))
            print i[0]
        except MySQLdb.Error as e:
            print  e
        conn.commit()



def divideTable():
    try:
        conn,cur=dbConnect()
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             #deleteUserTable = "DROP TABLE users_"+str(i)+str(j)
        #             #cur.execute(deleteUserTable)
        #             s="CREATE TABLE IF NOT EXISTS users_"+str(i)+str(j)+str(k)+"(\
        #                     uid VARCHAR(255) NOT NULL KEY,\
        #                     username VARCHAR(255),\
        #                     realname VARCHAR(255),\
        #                     location VARCHAR(255),\
        #                     photosurl VARCHAR(255),\
        #                     profileurl VARCHAR(255),\
        #                     photocount INT DEFAULT 0,\
        #                     firstdatetaken DATETIME,\
        #                     flag TINYINT NOT NULL DEFAULT 0)"
        #             cur.execute(s)
        #             s="CREATE UNIQUE INDEX uid ON "+ "users_"+str(i)+str(j)+str(k)+"(uid)"
        #             cur.execute(s)

        # userTab = []
        # for i in range(1000):
        #     userTab.append([])
        # try:
        #     count=0
        #     for i in range(9):
        #         userTable="users_"+str(i)
        #         s="SELECT uid,flag FROM "+userTable
        #         cur.execute(s)
        #         for uid in cur.fetchall():
        #             g=int(group(uid[0]))
        #             userTab[g].append((uid[0], uid[1])) # 返回的是一个元组，取第一个
        #             count+=1
        #     print count
        # except MySQLdb.Error as e:
        #     print e
        # conn.commit()

        # for i in range(1000):
        #     for j in userTab[i]:
        #         try:
        #             s="INSERT INTO users_"+str(i)+"(uid,flag) VALUES(%s,%s)"
        #             cur.execute(s,(j[0],j[1]))
        #             print j[0]
        #         except MySQLdb.Error as e:
        #             print  e
        #         conn.commit()


        # g=group("10001104@N00")
        # print g
        # print  "INSERT INTO users_" + g + "(uid,flag) VALUES(%s,%s)", ("10001104@N00", 1)
        # cur.execute("INSERT INTO users_"+g+"(uid,flag) VALUES(%  s,%s)",("10001104@N00",1))
        # conn.commit()
        for i in range(1000):
            cur.execute("DROP TABLE users_"+tablesId(i))
            conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print e

if __name__ == '__main__':
    divideTable()

