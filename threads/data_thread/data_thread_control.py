# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread,Lock
from reading_thread import ReadingThread
from writing_thread import WritingThread

class DataThreadControl(Thread):
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    def __init__(self, tableName):
        super(DataThreadControl, self).__init__()
        self.readingConn = None
        self.readingCur = None
        self.writingConn = None
        self.writingCur = None
        self.dbLock = Lock()
        self.tableName = tableName
        self.maxSQLLength = 100

    def setApi(self, api):
        self.api =api

    def setMaxSQL(self, maxNum):
        self.maxSQLLength = maxNum


    def setReadingQueue(self, readingQueue):
        self.readingQueue = readingQueue

    def setWritingQueue(self, writingQueue):
        self.writingQueue = writingQueue

    def setEntityQueue(self, entityQueue):
        self.entityQueue = entityQueue

    def run(self):
        self._runReadingAndWritingThread()
        while True:
            entity = self.entityQueue.get()
            if self._checkEntityQueue(entity):
                self.writingQueue.put(entity)
    
    def readingThreadInit(self):
        self._readingConnClose()
        self.readingThread = ReadingThread()
        self.readingThread.setApi(self.api)
        self.readingThread.setTableName(self.tableName)
        self.readingThread.setReadingQueue(self.readingQueue)

    def writingThreadInit(self):
        self._writingConnClose()
        self.writingThread = WritingThread()
        self.writingThread.setApi(self.api)
        self.writingThread.setTableName(self.tableName)
        self.writingThread.setWritingQueue(self.writingQueue)

    def _readingConnClose(self):
        if not self.readingConn == None:
            self.readingConn.close()
        if not self.readingCur == None:
            self.readingCur.close()
    
    def _writingConnClose(self):
        if not self.writingConn == None:
            self.writingConn.close()
        if not self.writingCur == None:
            self.writingCur.close()

    def _runReadingAndWritingThread(self):
        self.readingThreadInit()
        self.writingThreadInit()
        self.readingThread.start()
        self.writingThread.start()

    #检查元素是否符合要求
    def _checkEntityQueue(self, entity):
        if entity == None:
            return False
        if self.api == self.APILIST[0]:
            return entity.rules()
        elif self.api == self.APILIST[1]:
            return entity.rules()
        elif self.api == self.APILIST[2]:
            return entity.rules()
        elif self.api == self.APILIST[3]:
            return entity.rules()
        elif self.api == self.APILIST[4]:
            return entity.rules()



if __name__ == '__main__':
    pass