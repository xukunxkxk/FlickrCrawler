# __author__=xk
# -*- coding: utf-8 -*-
from time import time
from Queue import Queue
from threading import Lock
from time import sleep
import random
import logging
import logging.config
import os


class MyApp:
    APIKYELIMIT = 3600
    APITIMING = 3600

    def __init__(self):
        self.filePath = os.path.join(os.path.dirname(__file__) + r'\..\res\myApp')
        logFilepath = os.path.join(os.path.dirname(__file__), "../res/logging.conf")
        logging.config.fileConfig(logFilepath)
        self.logger = logging.getLogger("log")
        self.api_key = list()  # api_key
        self.secret = list()  # secret
        self.accessToken = list()  # accessToken
        self.time = list()  # 第一次调用时间
        self.remainCount = list()  # api剩余次数
        self.size = 0  # app个数
        self.appFile = None  # app文件
        self.lock = Lock()
        self.initApp()

    # 初始化App
    def initApp(self):
        while (1):
            # 加载app文件
            try:
                if (self.filePath):
                    self.appFile = open(self.filePath)  #
            except IOError as e:
                self.filePath = raw_input('File doesnt exist,try a another file path: ')
            else:
                break
        # 读入文件中的app
        try:
            data = self.appFile.readlines()
            self.appFile.close()
            i = 1
            for app in data:
                if i % 2 == 1:
                    self.api_key.append(app.strip('\n'))
                else:
                    self.secret.append(app.strip('\n'))
                    self.remainCount.append(self.APIKYELIMIT)
                i = i + 1
            # size  app个数
            self.size = len(self.remainCount)

            # 初始化时间
            for i in range(self.size):
                self.time.append(0)
        except IOError as e:
            print e
        self.logger.info('App Initialized Successfully')
        self.logger.info("%d App" % self.size)

    # 返回App
    def getApp(self):
        try:
            self.lock.acquire()
            # index = random.randint(0, self.size - 1)
            # return (self.api_key[index], self.secret[index])
            for i in range(self.size):
                # api次数小于限制
                if self.remainCount[i] > 0:
                    if self.remainCount[i] == self.APIKYELIMIT:
                        self.time[i] = time()
                    self.remainCount[i] -= 1
                    self.lock.release()
                    return (self.api_key[i], self.secret[i])
                # api次数大于限制,计算访问时间如超规定时间复位
                elif time() - self.time[i] >= self.APITIMING:
                    self.time[i] = self.APIKYELIMIT
            t = time()
            mintime = self.time[0]
            minIndex = 0
            for i in range(self.size):
                if self.time[i] < mintime:
                    minIndex = i
                    mintime = self.time[i]
            if t - mintime <= 3600:
                sleep(t - mintime)
                self.remainCount[minIndex] -= 1
                self.lock.release()
                return (self.api_key[minIndex], self.secret[minIndex])
        except IndexError as e:
            print e
            self.lock.release()
            self.getApp()
        except AttributeError as e:
            print e
            for i in range(self.size):
                self.remainCount[i] = self.APIKYELIMIT
            self.lock.release()
            self.getApp()

    def getApikey(self):
        try:
            return self.getApp()[0]
        except TypeError as e:
            self.getApikey()


if __name__ == '__main__':
    a = MyApp()
    print a.getApp()
    print a.time[0]
    print a.time[0]
    for i in range(3599):
        print  a.getApp()
    print a.getApp()
    print a.time[1]
