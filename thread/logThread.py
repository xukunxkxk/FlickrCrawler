# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from res.log import Log
from Queue import Queue
from time import sleep
from myException.ipLimitException import IpLimitException


class LogThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.logQueue = Queue()
        self.log = Log()

    def loggingUid(self):
        self.log.writeLog(self.logQueue.get())

    def getLogQueue(self):
        return self.logQueue

    def run(self):
        while 1:
            self.loggingUid()


if __name__ == '__main__':
    pass
