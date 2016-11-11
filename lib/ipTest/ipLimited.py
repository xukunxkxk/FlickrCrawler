# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError,urlopen
from bs4 import BeautifulSoup
import urllib2
class IpLimited:
    statTryCount = 0
    def __init__(self):
        self.stat = 1
    def ipLimitedTest(self):
        if self.stat == 0 :
            host = "https://api.flickr.com/services/rest/?"
            api = "flickr.people.getInfo"
            uid = "95200220@N03"
            api_key = "aed008500683ba19d27db0d9fc0b5bc6"
            try:
                self.statTryCount += 1
                html = urlopen(host + "&method=" + api + "&api_key=" + api_key + \
                              "&user_id=" + uid)  # proxies={'socket5':'127.0.0.1:1080'}
                returnData = BeautifulSoup(html, "html.parser")
                stat = str(returnData.find("rsp").attrs["stat"])
                if stat == 'ok':
                    self.statTryCount = 0
                    return True
            except AttributeError as e:
                self.statTryCount = 0
                return False
            except (HTTPError, IOError) as e:
                if self.statTryCount < 3:
                     return self.ipLimitedTest()
                else:
                    self.statTryCount = 0
                    self.stat = 1
                    return False
        elif self.stat == 1:
            host = "https://api.flickr.com/services/rest/?"
            api = "flickr.people.getInfo"
            uid = "95200220@N03"
            api_key = "b08c387d713a1ec32b6e22afb455ea56"
            try:
                self.statTryCount += 1
                html = urllib2.urlopen(host + "&method=" + api + "&api_key=" + api_key + \
                              "&user_id=" + uid)  # proxies={'socket5':'127.0.0.1:1080'}
                returnData = BeautifulSoup(html, "html.parser")
                stat = str(returnData.find("rsp").attrs["stat"])
                if stat == 'ok':
                    self.statTryCount = 0
                    return True
            except AttributeError as e:
                self.statTryCount = 0
                return False
            except (HTTPError, IOError) as e:
                if self.statTryCount < 3:
                     return self.ipLimitedTest()
                else:
                    self.statTryCount = 0
                    self.stat = 0
                    return False

    def test(self):
        if self.stat == 0 or self.stat == 1:
            if self.ipLimitedTest() or self.ipLimitedTest():
                return True
            else:
                self.stat = 3
                return False
        else:
            self.stat = 0
            return self.test()

    def setStat(self, stat):
        self.stat = stat
    def getStat(self):
        return self.stat



if __name__ == '__main__':
    limited = IpLimited()
    print limited.test()
    print limited.stat