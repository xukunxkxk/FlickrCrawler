# __author__=xk
# -*- coding: utf-8 -*-

from threading import Thread
from data_Thread.dataThreadControl import DataThreadControl
from spider_Thread.taskAllocation import TaskAllocation
from Queue import Queue
from lib.flickrApi.statCheck import StatCheck
from time import sleep
import logging
import logging.config
import os

class ThreadPool(Thread):
    POOLSIZE = 60
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    def __init__(self, tableName):
        super(ThreadPool, self).__init__()
        self.tableName = tableName
        self.spiderList = []

    def setApi(self, index):
        self.api = self.APILIST[index]

    def init(self):
        logFilePath = os.path.join(os.path.dirname(__file__), r"../res/logging.conf")
        logging.config.fileConfig(logFilePath)
        self.logger = logging.getLogger("log")

        self.spiderThreadPoolSize = self.POOLSIZE
        self.dataQueue = DataQueue()

        self.readingQueue = self.dataQueue.getReadingQueue()
        self.writingQueue = self.dataQueue.getWritingQueue()
        self.entityQueue = self.dataQueue.getEntityQueue()

        #数据管理线程初始化
        self.dataThreadControl = DataThreadControl(self.tableName)
        self.dataThreadControl.setApi(self.api)
        self.dataThreadControl.setReadingQueue(self.readingQueue)
        self.dataThreadControl.setWritingQueue(self.writingQueue)
        self.dataThreadControl.setEntityQueue(self.entityQueue)


        #爬虫管理线程初始化
        self.taskAllocation = TaskAllocation()
        self.taskAllocation.setApi(self.api)
        self.taskAllocation.setReadQueue(self.readingQueue)
        self.taskAllocation.setEntityQueue(self.entityQueue)

    def run(self):
        self.dataThreadControl.start()
        self._checkStat()
        self._initSpiderPoolThread(self.spiderThreadPoolSize)
        while True:
            self._spiderCheck()
            sleep(300)

    def _initSpiderPoolThread(self, spiderPoolSize):
        for x in xrange(spiderPoolSize):
            self._initSpiderThread()

    def _initSpiderThread(self):
        self.spiderList.append(self.taskAllocation.allocate())

    def _spiderCheck(self):
        self.logger.info("Running Spider Thread Check")
        removeList = []
        for spiderThread in self.spiderList:
            if not spiderThread.is_alive():
                removeList.append(spiderThread)
        self.logger.info("%s Threads Are Dead" % len(removeList))
        for spiderThread in removeList:
            self.spiderList.remove(spiderThread)
            self.spiderList.append(self.taskAllocation.allocate())
            self.logger.info("Has Init An New Thread")

    def _restart(self):
        pass

    def _checkStat(self):
        stat = StatCheck.get_stat()
        while stat == False:
            self.logger.info("Ip Limited Waiting 5 Minutes And Try Again!")
            sleep(300)


class DataQueue:
    def __init__(self):
        self.readingQueue = Queue()
        self.writingQueue = Queue(maxsize=200)
        self.entityQueue = Queue(maxsize=200)

    def getReadingQueue(self):
        return self.readingQueue

    def getWritingQueue(self):
        return self.writingQueue

    def getEntityQueue(self):
        return self.entityQueue


if __name__ == '__main__':
    threadPool = ThreadPool("users_1_copy")
    threadPool.setApi(1)
    threadPool.init()
    threadPool.start()