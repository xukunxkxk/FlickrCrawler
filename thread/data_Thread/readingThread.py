# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from db.dbConnect import dbConnect
from time import sleep
from exception.dbException import DBEmptyException
from exception.threadCrashException import ReadingThreadCrashExcetpion
import logging

import MySQLdb

def group(uid):
    return uid[uid.index(r'@') + 3]

class ReadingThread(Thread):
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    isOver = False

    def __init__(self):
        super(ReadingThread, self).__init__()
        self._connectDB()
        self.readingCount = 0
        #小于多少开始读数据库
        self.readingBound = 100
    
    def setApi(self, api):
        self.api = api
    
    def setReadingQueue(self, readingQueue):
        self.readingQueue = readingQueue

    def _connectDB(self):
        self.conn, self.cur = dbConnect()

    def _readDB(self):
        if self.api == self.APILIST[0] or self.api == self.APILIST[1] or self.api == self.APILIST[2]:
            self._readUid()
        elif self.api == self.APILIST[3] or self.api == self.APILIST[4]:
            self._readPhotoId()

    def _readUid(self):
        # try:
        #     self.readingCount=0
        #     self.cur.execute("SELECT uid FROM users WHERE flag <> 1 ")
        #     for uid in self.cur.fetchall():
        #         self.readingQueue.put(uid[0])   #返回的是一个元组，取第一个
        #         self.readingCount +=1
        #     self.conn.commit()
        #     print "Had Read %d uid" %self.readingCount
        #     return True
        # except MySQLdb.Error as e:
        #     return False

        # userFollowerApi
        # try:
        #     self.readingCount=0
        #     for i in range(9):
        #         userTable="users_"+str(i)
        #         s="SELECT uid FROM "+userTable+" WHERE flag <> 1"
        #         #s="SELECT uid FROM "+userTable+" WHERE flag <> 1 LIMIT 0,1000"
        #         self.cur.execute(s)
        #         for uid in self.cur.fetchall():
        #             self.readingQueue.put(uid[0])  # 返回的是一个元组，取第一个
        #             self.readingCount += 1
        #     self.conn.commit()
        #     if self.readingCount >= 0:
        #         print "Had Read %d uid" %self.readingCount
        #         return True
        #     else:
        #         return False
        # except MySQLdb.Error as e:
        #     return False

        try:
            # 返回错误用户
            self.readingCount = 0
            s = "SELECT uid FROM users_1_copy"
            self.cur.execute(s)
            for uid in self.cur.fetchall():
                self.readingQueue.put(uid[0])  # 返回的是一个元组，取第一个
                self.readingCount += 1
            self.conn.commit()
            if self.readingCount > 0:
                print "Had Read %d uid" % self.readingCount
            else:
                raise DBEmptyException("DB has no photoid")
        except MySQLdb.Error as e:
            print e

    def _readPhotoId(self):
        try:
            self.readingCount = 0
            s = "SELECT photoid FROM photos_1_copy WHERE flag = 1  limit 0,1000000"
            self.cur.execute(s)
            for uid in self.cur.fetchall():
                self.readingQueue.put(uid[0])  # 返回的是一个元组，取第一个
                self.readingCount += 1
            self.conn.commit()
            if self.readingCount > 0:
                print "Had Read %d photoid" % self.readingCount
            else:
                raise DBEmptyException("DB has no photoid")
        except MySQLdb.Error as e:
            print e

    def run(self):
        try:
            self._running()
        except Exception as e:
            print e
            raise ReadingThreadCrashExcetpion("Error: Reading Thread Has Been Crashed!")

    def _running(self):
        while True:
            try:
                while self.readingQueue.qsize() >= self.readingBound or self.readingBound == -1:
                    sleep(10)
                self._readDB()
            except DBEmptyException as e:
                logging.warn(e.msg)
                self.readingBound = -1


    def closeConn(self):
        self.conn.close()
        self.cur.close()

    def getConn(self):
        return self.conn, self.cur





if __name__ == '__main__':
    from Queue import Queue
    r = ReadingThread()
    r.setApi("photoUrl")
    r.setReadingQueue(Queue())
    r.start()