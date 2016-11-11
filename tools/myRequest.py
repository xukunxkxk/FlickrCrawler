# __author__=xk
# -*- coding: utf-8 -*-
from urllib import urlencode
from urllib2 import urlopen,Request
from bs4 import BeautifulSoup
from myGzip import gzipDecode
import urllib2
import sys


class Requests:
    html = None
    def __init__(self):
        self.opener = None
        self.bsoj = None
        self.url = None
        self.html = None
        self.data ={}
        self.encode = "utf-8"
        reload(sys)
        sys.setdefaultencoding('utf-8')

    def get(self,url):
        self.url = url
        self.html = urlopen(url = url)
        self.bsoj = BeautifulSoup(self.html, "html.parser")
        return self.bsoj

    def getBSObjet(self):
        if self.bsoj:
            return self.bsoj
        else:
            return None

    def getLabel(self, label):
        return self.bsoj.find(label)

    def getAllLabel(self, label):
        return self.bsoj.findAll(label)


    def getAttrsValue(self, label, attrs):
        return str(self.bsoj.find(label)[attrs])

    def getAllAttrsValue(self, label, attrs):
        attrsList = []
        for element in self.bsoj.findAll(label):
            attrsList.append(str(element[attrs]))
        return attrsList


    def getText(self, label, attrs = None, id = None):
        if id:
            return str(self.bsoj.find(label,{attrs : id}).get_text())
        else:
            return str(self.bsoj.find(label).get_text())

    def getAllText(self, label, attrs = None , id = None):
        if id:
            attrsList = []
            for element in self.bsoj.findAll(label,{attrs : id}):
                attrsList.append(str(element.get_text()))
            return attrsList
        else:
            attrsList = []
            for element in self.bsoj.findAll(label):
                attrsList.append(str(element.get_text()))
            return attrsList



    def post(self, url, data = None ):
        pass

    def getUrl(self):
        return self.html.geturl()



if __name__ == '__main__':
    request = Requests()
    # html = request.get("https://api.flickr.com/services/rest/?&method=flickr.people.getInfo&api_key=0b20e726fd5a04cb2be8a7177f20deac&user_id=95200220@N03")
    URL = "https://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&api_key=e6e96eed7af7deb2d35cac2e3739ed7d&user_id=100007433@N06&per_page=500&page=1"
    request.get("https://www.taobao.com/")
    print request.bsoj
