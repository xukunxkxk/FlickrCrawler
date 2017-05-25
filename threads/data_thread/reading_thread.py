# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from db.db_connect import dbConnect
from time import sleep
from exception.db_exception import DBEmptyException
from exception.thread_crash_exception import ReadingThreadCrashExcetpion
import logging
import logging.config
import os

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
        logFilePath = os.path.join(os.path.dirname(__file__), "../../res/logging.conf")
        logging.config.fileConfig(logFilePath)
        self.logger = logging.getLogger("log")

    def setTableName(self, tableName):
        self.tableName = tableName

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
        #     self.logger.info("Had Read %d uid" %self.readingCount)
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
        #         self.logger.info("Had Read %d uid" %self.readingCount)
        #         return True
        #     else:
        #         return False
        # except MySQLdb.Error as e:
        #     return False

        try:
            # 返回错误用户
            self.readingCount = 0
            s = "SELECT uid FROM " + self.tableName
            self.cur.execute(s)
            for uid in self.cur.fetchall():
                self.readingQueue.put(uid[0])  # 返回的是一个元组，取第一个
                self.readingCount += 1
            self.conn.commit()
            if self.readingCount > 0:
                self.logger.info("Had Read %d uid" % self.readingCount)
            else:
                raise DBEmptyException("DB has no uid")
        except MySQLdb.Error as e:
            self.logger.error(e)

    def _readPhotoId(self):
        try:
            self.readingCount = 0
            s = "select photoid from " + self.tableName +" where flag = 1 limit 10000"
            self.cur.execute(s)
            tempList = []
            for photoid in self.cur.fetchall():
                tempList.append(photoid[0]) # 返回的是一个元组，取第一个
                self.readingCount += 1
            self.conn.commit()
            writingUrl = "update " + self.tableName + " set flag = 2 where flag = 1 limit 10000"
            self.cur.execute(writingUrl)
            self.conn.commit()
            for photoid in tempList:
                self.readingQueue.put(photoid)
            if self.readingCount > 0:
                self.logger.info("Had Read %d photoid" % self.readingCount)
            else:
                raise DBEmptyException("DB has no photoid!")
        except MySQLdb.Error as e:
            self.logger.error(e)

    def run(self):
        self.logger.info("Reading Thread Has been started")
        self._cleanFailureFlag()
        try:
            self._running()
        except Exception as e:
            print e
            self.logger.error(e)
            raise ReadingThreadCrashExcetpion("Error: Reading Thread Has Been Crashed!")

    def _running(self):
        while True:
            try:
                while self.readingQueue.qsize() >= self.readingBound or self.readingBound == -1:
                    sleep(10)
                self._readDB()
            except DBEmptyException as e:
                self.logger.error(e.msg)
                self.readingBound = -1

    def _cleanFailureFlag(self):
        if self.api == self.APILIST[4]:
            logFilePath = os.path.join(os.path.dirname(__file__), r"../../res/notExitId.log")
            notExitPhotoIdLog = open(logFilePath, "r")
            notExitPhotoIdList = []
            for line in notExitPhotoIdLog.readlines():
                photoid = line.strip("\n")
                notExitPhotoIdList.append((photoid,))
            sql = "update " + self.tableName + " set flag = 3 where photoid=%s"
            try:
                self.cur.executemany(sql, notExitPhotoIdList)
                self.conn.commit()
                self.logger.info("None exists Url Has Been Coped")
            except MySQLdb.Error as e:
                self.logger.error(e)
            notExitPhotoIdLog = open(logFilePath, "w")
            notExitPhotoIdLog.write("")


            sql = "update " + self.tableName + " set flag = 1 where flag = 2 and downloadurl is null"
            try:
                self.cur.execute(sql)
                self.conn.commit()
                self.logger.info("Failure Download Url Has Been Rewind")
            except MySQLdb.Error as e:
                self.logger.error(e)

            sql = "update " + self.tableName + " set flag = 0 where flag = 2 "
            try:
                self.cur.execute(sql)
                self.conn.commit()
                self.logger.info("Success Download Url Has Been Update")
            except MySQLdb.Error as e:
                self.logger.error(e)


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