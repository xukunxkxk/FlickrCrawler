# __author__=xk
# -*- coding: utf-8 -*-
import re
# from urllib import urlopen
from urllib2 import HTTPError, urlopen
from bs4 import BeautifulSoup
from tools.myApp import MyApp
import urllib2


class Stat:
    statTryCount = 0
    # myApp = MyApp()
    def __init__(self):
        pass

    @staticmethod
    def get_stat():
        host = "https://api.flickr.com/services/rest/?"
        # api_key = Stat.myApp.getApikey()
        api = "flickr.contacts.getPublicList"
        uid = "95200220@N03"
        page = '1'
        api_key = "7bed02742a91566413039b76e7cc3c46"
        isWrong = False
        try:
            Stat.statTryCount += 1
            html = urlopen(host + "&method=" + api + "&api_key=" + api_key + \
                           "&user_id=" + uid + "&page=" + page)  # proxies={'socket5':'127.0.0.1:1080'}
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
