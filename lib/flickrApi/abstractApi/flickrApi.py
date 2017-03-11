# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError
from tools.myRequest import Requests
from exception.ipLimitedException import IpLimitedExcetpion
from entity.flickrEntity import *
import logging
import logging.config
import os

class AbstractFlickrApi(object):
    def __init__(self):
        self.request = Requests()
        self.stat = True
        self.host = "https://api.flickr.com/services/rest/?"
        self.api = None
        self.webData = None
        self.entity = None
        self.exits = True
        self.taskList = []
        self.apiName = str(self.__class__).split(".")[1][:-2]
        logFilePath = os.path.join(os.path.dirname(__file__), "../../../res/logging.conf")
        logging.config.fileConfig(logFilePath)
        self.logger = logging.getLogger("log")

    def setApp(self, app):
        self.app = app

    def setTaskId(self, taskId, apiName=None):
        self.taskId = taskId
        if apiName:
            self.entity = eval(apiName + "Entity")(self.taskId)
        else:
            self.entity = eval(self.apiName + "Entity")(self.taskId)

    def work(self):
        try:
            self._get()
            self._statCheck()
        #爬取出现异常，分析并处理
        except (HTTPError, IOError) as errorMsg:
            logging.error(str(errorMsg) + self.taskId)
            self._exceptionCheck(errorMsg)
            return None

        #正常爬取
        if self.exits and self._webDataCheck():
            self.analyze()
            return self.entity
        else:
            return None

    def getStat(self):
        return self.stat

    #分析返回页面
    def analyze(self):
        pass

    #覆盖爬取地址
    def getAddress(self):
        pass


    def _taskListCheck(self):
        if len(self.taskList) != 0:
            self._work()

    def _work(self):
        for html in self.taskList:
            self._get(html)
            self.analyze()
        self.taskList = []


    def _get(self, html=None):
        if html == None:
            htmlAddress = self.getAddress()
        else:
            htmlAddress = html
        self.request.get(htmlAddress)
        self.webData = self.request.getBSObjet()

    # 检查返回数据状态,判断是否ip被封
    def _statCheck(self):
        try:
            self.stat = str(self.request.getAttrsValue('rsp', 'stat'))
            if self.stat == "fail":
                self.stat = True
                self.exits = False
            elif self.stat == "ok":
                self.stat = True
        except AttributeError:
            self.stat = False

    def _exceptionCheck(self, errorMsg):
        if str(errorMsg) == "HTTP Error 429: ":
            self.stat = False
            raise IpLimitedExcetpion("HTTP Error 429: ")
        elif str(errorMsg) == r"HTTP Error 418: I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\nHTTP/1.0 418 I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\n":
            self.stat = False
            raise IpLimitedExcetpion("HTTP Error 418: Teapot Error")
        else:
            pass

    def _webDataCheck(self):
        if not self.webData:
            return False
        else:
            return True

if __name__ == '__main__':
    a = AbstractFlickrApi()
    a.setTaskId("1111")