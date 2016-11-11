# __author__=xk
# -*- coding: utf-8 -*-
'写数据库'
import MySQLdb

def group(uid):
    return uid[uid.index(r'@')+3]

class DBRead:
    APILIST = ["userFollowers", "userInformation"]
    def __init__(self,readQueue,api,conn,cur,):
        self.readQueue=readQueue
        self.api=api
        self.conn=conn
        self.cur=cur
        self.count=0
    def readDB(self):
        if self.api == self.APILIST[0] or self.api == self.APILIST[1]:
            return self.readUid()

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

        #userFollowerApi
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
            self.count = 0
            for i in range(5,9):
                userTable = "users_" + str(i)
                s = "SELECT uid FROM " + userTable + " WHERE username IS NULL and flag = 1"
                self.cur.execute(s)
                for uid in self.cur.fetchall():
                    self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
                    self.count += 1
            self.conn.commit()
            if self.count >= 0:
                print "Had Read %d uid" %self.count
                return True
            else:
                return False

            ##返回错误用户
            # self.count = 0
            # s = "SELECT uid FROM users_5 WHERE username IS NULL"
            # self.cur.execute(s)
            # for uid in self.cur.fetchall():
            #     self.readQueue.put(uid[0])  # 返回的是一个元组，取第一个
            #     self.count += 1
            # self.conn.commit()
            # if self.count >= 0:
            #     print "Had Read %d uid" %self.count
            #     return True
            # else:
            #     return False
        except MySQLdb.Error as e:
            return False

    def setDBConn(self,conn):
        self.conn=conn
    def setDBcur(self,cur):
        self.cur=cur




if __name__ == '__main__':
    from db.dbConnect import dbConnect
    from  Queue import  Queue
    readQueue = Queue()
    conn,cur = dbConnect()
    dbR = DBRead(readQueue,"userInformation",conn,cur)
    dbR.readUid()
    len = readQueue.qsize()
    for i in range(1000):
        print readQueue.get()



