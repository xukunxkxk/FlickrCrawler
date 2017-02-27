# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError
from tools.myRequest import Requests

class FlickrApi(object):
    def __init__(self, app):
        self.request = Requests()
        self.app = app
        self.stat = True
        self.host = "https://api.flickr.com/services/rest/?"
        self.api = None
        self.webData = None
        self.entity = None
        self.exits = True

    def work(self):
        try:
            self._get()
            self._statCheck()
        except (HTTPError, IOError) as e:
            #检测HTTP ERROR  若429 则暂停爬取
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False
            elif str(e) == r"HTTP Error 418: I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\nHTTP/1.0 418 I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\n":
                self.stat = False
            return None

        if not self.webData:
            return None
        else:
            self.analyze()
            return self.entity


    def getStat(self):
        return self.stat

    def analyze(self):
        pass

    def getAddress(self):
        pass

    def _get(self):
        htmlAddress = self.getAddress()
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




if __name__ == '__main__':
    pass