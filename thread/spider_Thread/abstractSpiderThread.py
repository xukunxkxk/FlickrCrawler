# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from lib.flickrApi.api import *



from time import sleep
from exception.ipLimitedException import IpLimitedExcetpion
from lib.flickrApi.statCheck import StatCheck

class AbstractSpiderThread(Thread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(AbstractSpiderThread, self).__init__()
        self.app = app
        self.entityQueue = entityQueue
        self.taskAllocation = taskAllocation
        self.stat = True

    def run(self):
        while True:
            self._setSpider()
            #检测网站是否封ip
            self._statCheck()
            self._spiderWork()

    def _setSpider(self):
        #未对taskAllocation变量加锁
        taskId = self.taskAllocation.getTask()
        self.spider = self._initSpider()
        self.spider.setApp(self.app)
        self.spider.setTaskId(taskId, self.apiName)

    def _initSpider(self):
        self.apiName = str(self.__class__).split(".")[-1].strip("'>")[:-6]
        return eval(self.apiName+"()")

    def _statCheck(self):
        while self.stat == False:
            sleep(300)
            self.stat = StatCheck.get_stat()

    def _spiderWork(self):
        try:
            entity = self.spider.work()
            if entity != None:
                self.entityQueue.put(entity)
        except IpLimitedExcetpion as e:
            print e.msg
            self.stat = False


if __name__ == '__main__':
    from Queue import Queue
    q = Queue()
    a = AbstractSpiderThread("", "", q)
