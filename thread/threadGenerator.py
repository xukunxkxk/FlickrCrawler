# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread, Lock
from time import sleep
from apiCallThread import ApiCallThread
from dataThread import DataThread
from logThread import LogThread
from lib.flickrApi.stat import Stat
from myException.ipLimitException import IpLimitException
from lib.ipTest.ipLimited import IpLimited
from ipLimitedThread import IpLimitedDectedThread


class ThreadGenerator(Thread):
    maxConcurrentThreadCount = 160

    def __init__(self, api):
        Thread.__init__(self)
        self.api = api
        self.logThread = LogThread()
        # self.ipLimited = IpLimited()
        # self.ipLimitedThread = IpLimitedDectedThread()
        self.logQueue = self.logThread.getLogQueue()
        self.dataThread = DataThread(api, self.logQueue)
        self.readQueue = self.dataThread.getReadQueue()
        self.writeQueue = self.dataThread.getWriteQueue()
        self.app = self.dataThread.getApp()

    def run(self):
        while 1:
            if Stat.get_stat():
                break
            else:
                print "Not Ready"
                sleep(600)
        self.dataThread.start()
        self.threadInit()
        self.logThread.start()
        # self.ipLimitedThread,start()

    def threadInit(self):
        for i in range(self.maxConcurrentThreadCount):
            try:
                ApiCallThread(self.readQueue, self.writeQueue, self.api, self.app).start()
            except Exception as e:
                sleep(1)
                ApiCallThread(self.readQueue, self.writeQueue, self.api, self.app).start()


if __name__ == '__main__':
    threadGenerator = ThreadGenerator("userPhotos")
    threadGenerator.start()
