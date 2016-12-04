# __author__=xk
# -*- coding: utf-8 -*-
'写数据库'
import MySQLdb


def group(uid):
    return uid[uid.index(r'@') + 3]


class DBRead:
    APILIST = ["userFollowers", "userInformation", "userPhotos", "photoSize"]

    def __init__(self, readQueue, api, conn, cur):
        self.readQueue = readQueue
        self.api = api
        self.conn = conn
        self.cur = cur
        self.count = 0

    def readDB(self):
        if self.api == self.APILIST[0] or self.api == self.APILIST[1] or self.api == self.APILIST[2]:
            return self.readUid()
        elif self.api == self.APILIST[3]:
            return self.readPhotoId()

    def readUid(self):
        # try:
        #     self.count=0
        #     self.cur.execute("SELECT uid FROM users WHERE flag <> 1 ")
        #     for uid in self.cur.fetchall():
        #         self.readQueue.put(uid[0])   #返回的是一个元组，取第一个
        #         self.count +=1
        #     self.conn.commit()
        #     print "Had Read %d uid" %self.count
        #     return True
        # except MySQLdb.Error as e:
        #     return False

        # userFollowerApi
        # try:
        #     self.count=0
        #     for i in range(9):
        #         userTable="users_"+str(i)
        #         s="SELECT uid FROM "+userTable+" WHERE flag <> 1"
        #         #s="SELECT uid FROM "+userTable+" WHERE flag <> 1 LIMIT 0,1000"
        #         self.cur.execute(s)
        #         for uid in self.cur.fetchall():
        #             self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
        #             self.count += 1
        #     self.conn.commit()
        #     if self.count >= 0:
        #         print "Had Read %d uid" %self.count
        #         return True
        #     else:
        #         return False
        # except MySQLdb.Error as e:
        #     return False

        try:
            # self.count = 0
            # for i in range(0,9):
            #     userTable = "users_" + str(i)
            #     s = "SELECT uid FROM " + userTable + " WHERE username IS NOT NULL AND flag = 0"
            #     self.cur.execute(s)
            #     for uid in self.cur.fetchall():
            #         self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
            #         self.count += 1
            # self.conn.commit()
            # if self.count >= 0:
            #     print "Had Read %d uid" %self.count
            #     return True
            # else:
            #     return False

            # 返回错误用户
            self.count = 0
            # s = "SELECT uid FROM users_0 WHERE username IS NOT NULL AND flag = 0 LIMIT 0,1000"
            s = "SELECT uid FROM users_8 WHERE username IS NOT NULL AND flag = 0"
            self.cur.execute(s)
            for uid in self.cur.fetchall():
                self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
                self.count += 1
            self.conn.commit()
            if self.count >= 0:
                print "Had Read %d uid" % self.count
                return True
            else:
                return False
        except MySQLdb.Error as e:
            return False

    def readPhotoId(self):
        try:
            self.count = 0
            s = "SELECT photoid FROM photos_0 WHERE flag = 0"
            self.cur.execute(s)
            for uid in self.cur.fetchall():
                self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
                self.count += 1
            self.conn.commit()
            if self.count >= 0:
                print "Had Read %d uid" % self.count
                return True
            else:
                return False
        except MySQLdb.Error as e:
            return False

    def setDBConn(self, conn):
        self.conn = conn

    def setDBcur(self, cur):
        self.cur = cur


if __name__ == '__main__':
    from db.dbConnect import dbConnect
    from  Queue import Queue

    readQueue = Queue()
    conn, cur = dbConnect()
    dbR = DBRead(readQueue, "userPhotos", conn, cur)
    dbR.readUid()
    len = readQueue.qsize()
    for i in range(1000):
        print readQueue.get()
