# __author__=xk
# -*- coding: utf-8 -*-
import re
from myException.ipLimitException import IpLimitException
# from urllib import urlopen
from urllib2 import HTTPError,urlopen
from bs4 import BeautifulSoup
import urllib2
class Stat:
    statTryCount = 0
    def __init__(self):
        pass

    @staticmethod
    def get_stat():
        host = "https://api.flickr.com/services/rest/?"
        api = "flickr.contacts.getPublicList"
        uid = "95200220@N03"
        page = '1'
        api_key = "b08c387d713a1ec32b6e22afb455ea56"
        isWrong = False
        try:
            Stat.statTryCount += 1
            html = urlopen(host + "&method=" + api + "&api_key=" + api_key + \
                           "&user_id=" + uid + "&page=" + page)#proxies={'socket5':'127.0.0.1:1080'}
            returnData = BeautifulSoup(html, "html.parser")
            stat = str(returnData.find("rsp").attrs["stat"])
            if stat == 'ok':
                Stat.statTryCount = 0
                return True
        except AttributeError as e:
            Stat.statTryCount = 0
            return False
        except (HTTPError, IOError) as e:
            if Stat.statTryCount < 3:
                return Stat.get_stat()
            else:
                Stat.statTryCount = 0
                return False


if __name__ == '__main__':
    print Stat.get_stat()