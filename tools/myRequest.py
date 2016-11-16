# __author__=xk
# -*- coding: utf-8 -*-
from urllib import urlencode
from urllib2 import urlopen,Request
from bs4 import BeautifulSoup
from myGzip import gzipDecode
import urllib2,cookielib
import sys
import re

class Requests:
    html = None
    def __init__(self):
        self.bsoj = None
        self.url = None
        self.html = None
        self.data ={}
        self.encode = "utf-8"
        self.lastDomainUrl = None

        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))

        reload(sys)
        sys.setdefaultencoding('utf-8')

    def get(self, url, fraud = False, encoding = None):
        self.url = url
        if not fraud:
            self.html = urlopen(url = url)
        else:
            header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
            req = urllib2.Request(url, headers = header)
            self.html = urlopen((req))
        if not encoding:
            self.bsoj = BeautifulSoup(self.html, "html.parser")
        else:
            self.bsoj = BeautifulSoup(self.html, "html.parser", from_encoding = encoding)
        return self.bsoj


    def post(self, url, formData = None, headers = None, gzip = False, encoding = None):
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
        postData = urlencode(formData)
        req = urllib2.Request(url, postData, headers)
        self.html = self.opener.open(req).read()
        if gzip:
            if encoding:
                self.bsoj = BeautifulSoup(gzipDecode(self.html), "html.parser", from_encoding = encoding)
            else:
                self.bsoj = BeautifulSoup(gzipDecode(self.html), "html.parser")
        else:
            if encoding:
                self.bsoj = BeautifulSoup(self.html, "html.parser", from_encoding = encoding)
            else:
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

    def getAttrsValue(self, label, attrs, regex = None):
        if not regex:
            return str(self.bsoj.find(label)[attrs])
        else:
            return str(self.bsoj.find(label, {attrs : re.compile(regex)})[attrs])

    def getAllAttrsValue(self, label, attrs, regx = None):
        if not regx:
            attrsList = []
            for element in self.bsoj.findAll(label):
                if element.has_attr(attrs):
                    attrsList.append(str(element[attrs]))
            return attrsList
        else:
            attrsList = []
            for element in self.bsoj.findAll(label, {attrs: re.compile(regx)}):
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






    def getUrl(self):
        url =  str(self.html.geturl())
        pattern = re.compile("\S*/")
        match = pattern.search(url)
        if match:
            self.lastDomainUrl =  match.group()
        return url

    def getPreDomain(self):
        self.getUrl()
        return self.lastDomainUrl


if __name__ == '__main__':
    request = Requests()
    # html = request.get("https://api.flickr.com/services/rest/?&method=flickr.people.getInfo&api_key=0b20e726fd5a04cb2be8a7177f20deac&user_id=95200220@N03")
    # request.get("http://cl.dh4.biz/index.php", fraud = True, encoding = "gbk")
    # print request.getAllLabel('a')
    # lastDomainUrl =  request.getPreDomain()
    # for url in request.getAllAttrsValue('a', 'href'):
    #     print lastDomainUrl + url


    #posttest
    url = "https://login.yahoo.com/config/login?.src=flickrsignin"
    request.get(url)

    e = request.getBSObjet().findAll('input', {'type': 'hidden'})
    formData = {}
    for values in e:
        formData[str(values['name'])] = str(values['value'])
    formData['passwd'] = 'sbdydd7z'
    formData['username'] = 'xukunxkxk'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': r'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep - alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'login.yahoo.com',
        'Origin': 'https://login.yahoo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'X-Requested-With': 'XMLHttpRequest'
    }
    loginUrl = "https://login.yahoo.com/config/login?.src=flickrsignin"
    request.post(loginUrl, formData, headers, True)
