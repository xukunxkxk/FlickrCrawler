# __author__=xk
# -*- coding: utf-8 -*-
from Queue import Queue
from threading import Thread
from time import sleep
from db.dbConnect import dbConnect
from db.dbWrite import DBWrite
from tools.myApp import MyApp


class WritingThread(Thread):
    writingDBBound = 1
    APILIST = ["userFollowers", "userInformation", "userPhotos", "photoInformation"]

    def __init__(self, api,writeQueue, logQueue):
        Thread.__init__(self)

        self.logQueue = logQueue
        self.isLimit = 0

        # 写队列
        self.writeQueue = writeQueue
        self.api = api
        # 初始化数据库
        self.conn, self.cur = dbConnect()

        self.app = MyApp()

        # 初始化数据库Writer
        self.dbWriter = DBWrite(self.writeQueue, self.logQueue, self.conn, self.cur)

    # 读写线程函数
    def dataThreadRunning(self):
        try:
            if self.writeQueue.qsize() >= self.writingDBBound:
                self.dbWriter.writeDB()
        except RuntimeError as e:
            print "RuntimeError Happened WritingThread Will be Started In 1 Second"
            sleep(1)

    def reSetDBRandW(self):
        self.dbWriter.setDBConn(self.conn)
        self.dbWriter.setDBcur(self.cur)

    # 读写线程
    def run(self):
        while 1:
            try:
                self.dataThreadRunning()
            except Exception as e:
                print e, " Happened In WritingThread!"
                if self.cur:
                    self.cur.close()
                if self.conn:
                    self.conn.close()
                self.conn, self.cur = dbConnect()
                self.reSetDBRandW()
                sleep(1)


    def getWriteQueue(self):
        return self.writeQueue

    def getApi(self):
        return self.api

    def getApp(self):
        return self.app


if __name__ == '__main__':
    pass
