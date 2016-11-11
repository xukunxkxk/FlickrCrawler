# __author__=xk
# -*- coding: utf-8 -*-
from db.dbConnect import dbConnect
from db.dbRead import DBRead
from db.dbWrite import DBWrite
from res.myApp import MyApp
from Queue import Queue
from time import sleep
from apiCallThread import ApiCallThread
from threading import Thread

class DataThread(Thread):
    readingDBBound=0
    writingDBBound=1
    APILIST = ["userFollowers", "userInformation"]
    def __init__(self,api,logQueue):
        Thread.__init__(self)
        self.isReadOver = False




        self.logQueue = logQueue
        self.isLimit = 0

        # 初始化读写队列
        self.readQueue=Queue()
        self.writeQueue=Queue(maxsize=100)
        self.api = api
        #初始化数据库
        self.conn, self.cur = dbConnect()

        self.app = MyApp()

        #初始化数据库Reader & Writer
        self.dbReader=DBRead(self.readQueue,self.api,self.conn,self.cur)
        self.dbWriter=DBWrite(self.writeQueue,self.logQueue,self.conn,self.cur)
        #预读数据库
        self.dbReader.readDB()

    #读写线程函数
    def dataThreadRunning(self):
        try:
            if self.writeQueue.qsize() >= self.writingDBBound:
                self.dbWriter.writeDB()
                #ApiCallThread(self.readQueue, self.writeQueue, self.api, self.app).start()
                #启动线程
                if not self.isReadOver:
                    if self.readQueue.qsize() < self.readingDBBound:
                        if not self.dbReader.readDB():
                            self.isReadOver = True
        except RuntimeError as e:
            print "RuntimeError Happened DataTread Will be Started In 1 Second"
            sleep(1)

    def reSetDBRandW(self):
        self.dbReader.setDBConn(self.conn)
        self.dbReader.setDBcur(self.cur)
        self.dbWriter.setDBConn(self.conn)
        self.dbWriter.setDBcur(self.cur)
    #读写线程
    def run(self):
        while 1:
            try:
                self.dataThreadRunning()
            except Exception as e:
                print e," Happened In DataThread!"
                if self.cur:
                    self.cur.close()
                if self.conn:
                    self.conn.close()
                self.conn, self.cur = dbConnect()
                self.reSetDBRandW()
                sleep(1)


    def getReadQueue(self):
        return self.readQueue
    def getWriteQueue(self):
        return self.writeQueue
    def getApi(self):
        return self.api
    def getApp(self):
        return self.app


if __name__ == '__main__':

    app=MyApp()
    dataThread=DataThread("userFollowers")
    apiThread=ApiCallThread(dataThread.getReadQueue(),dataThread.getWriteQueue(),dataThread.getApi(),app)
    dataThread.start()
    apiThread.start()
