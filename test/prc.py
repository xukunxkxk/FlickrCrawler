# __author__=xk
# -*- coding: utf-8 -*-
from time import ctime,strftime,localtime
import urllib,urllib2,cookielib
from urllib2 import urlopen
import StringIO, gzip
from  bs4 import BeautifulSoup
from threading import Thread,Lock
import re
def gzdecode(data) :
    compressedstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()   # 读取解压缩后数据
    return data2

    # cookieJar = cookielib.CookieJar()
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    # url = "https://login.yahoo.com/config/login?.src=flickrsignin"
    # response = opener.open(url).read()
    # bsoj = BeautifulSoup(response, "html.parser", from_encoding='gzip')
    # e = bsoj.find('div',{'class':'hidden'})
    # e = bsoj.findAll('input',{'type':'hidden'})
    # formData = {}
    # for values in e:
    #     formData[str(values['name'])] = str(values['value'])
    #
    # loginUrl ="https://login.yahoo.com/config/login?.src=flickrsignin"
    #
    # opener.addheaders =[('Accept','*/*'),
    #                     ('Accept-Encoding', r'gzip, deflate, br'),
    #                     ('Accept-Language','zh-CN,zh;q=0.8'),
    #                     ('Cache-Control','no-cache'),
    #                     ('Connection', r'keep - alive'),
    #                     ('Content-Type','application/x-www-form-urlencoded; charset=UTF-8'),
    #                     ('Host', 'login.yahoo.com'),
    #                     ('Origin', 'https://login.yahoo.com'),
    #                     #('Referer','https://login.yahoo.com/config/login?.src=flickrsignin&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dcn%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252Fservices%25252Fapps%25252Fby%25252Fxukunxkxk'),
    #                     ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'),
    #                     ('X-Requested-With','XMLHttpRequest')
    #                     ]
    # formData['passwd']='sbdydd7z'
    # formData['username']='xukunxkxk'
    # formData =urllib.urlencode(formData)
    # response = opener.open(loginUrl,formData)
    #
    # html = opener.open("https://www.flickr.com/services/apps/create/noncommercial/?").read()
    # createApiUrl = 'https://www.flickr.com/services/apps/create/noncommercial/'
    # response = opener.open(createApiUrl,urllib.urlencode({'app_name':'1','app_description':'1','agrees_to_respect':'1','agrees_to_tos':'1'})).read()
    # print gzdecode(response)

def getApiKey(knoc,appFile):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    url = "https://login.yahoo.com/config/login?.src=flickrsignin"

    response = urlopen(url)

    content = response.read()
    bsoj = BeautifulSoup(content, "html.parser", from_encoding='gzip')
    e = bsoj.find('div', {'class': 'hidden'})
    e = bsoj.findAll('input', {'type': 'hidden'})

    formData = {}
    for values in e:
        formData[str(values['name'])] = str(values['value'])
    formData['passwd']='sbdydd7z'
    formData['username']='xukunxkxk'
    formData =urllib.urlencode(formData)

    headers = {
        'Accept':'*/*',
        'Accept-Encoding':r'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection': 'keep - alive',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'login.yahoo.com',
        'Origin':'https://login.yahoo.com',
        #('Referer','https://login.yahoo.com/config/login?.src=flickrsignin&mg=1&.done=https%3A%2F%2Flogin.yahoo.com%2Fconfig%2Fvalidate%3F.src%3Dflickrsignin%26.pc%3D8190%26.scrumb%3D0%26.pd%3Dc%253DJvVF95K62e6PzdPu7MBv2V8-%26.intl%3Dcn%26.done%3Dhttps%253A%252F%252Fwww.flickr.com%252Fsignin%252Fyahoo%252F%253Fredir%253Dhttps%25253A%25252F%25252Fwww.flickr.com%25252Fservices%25252Fapps%25252Fby%25252Fxukunxkxk'),
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'X-Requested-With':'XMLHttpRequest'
    }

    loginUrl = "https://login.yahoo.com/config/login?.src=flickrsignin"
    req = urllib2.Request(loginUrl, formData, headers)
    opener.open(req)
    # 注册apikey
    createApiakyUrl = "https://www.flickr.com/services/apps/create/noncommercial/?"
    html = opener.open(createApiakyUrl).read()
    bsoj = BeautifulSoup(html, "html.parser")
    magic_cookie = str(bsoj.find('input', {'name': 'magic_cookie'}).attrs['value'])
    #print magic_cookie

    while 1:  # 得到magic_cookie
        try:
            formData = {
            'magic_cookie': magic_cookie,
            'done': '1',
            'app_name': '1',
            'app_description': '1',
            'agrees_to_respect': '1',
            'agrees_to_tos': '1'
            }
            formData = urllib.urlencode(formData)
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': r'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'origin': 'https://www.flickr.com',
            'pragma': 'no-cache',
            'referer': 'https://www.flickr.com/services/apps/create/noncommercial/',
            'upgrade-insecure-requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
            }
            req = urllib2.Request(createApiakyUrl, formData, headers)
            content = opener.open(req).read()
            bsoj = BeautifulSoup(gzdecode(content), "html5lib")
            knoc.acquire()
            for elements in bsoj.findAll('span', {'class': 'api-key-info'}):
                text = str(elements.get_text())
                try:
                    appFile.write(text)
                    appFile.write('\n')
                    appFile.flush()
                except IOError:
                    appFile.close()
                    appFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\myApp','a')
                    appFile.write(text)
                    appFile.write('\n')
                    appFile.flush()
                print text
            knoc.release()
        except Exception as e:
            print e

if __name__ == '__main__':
    lock = Lock()
    appFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\myApp','a')
    appFile.flush()
    for i in range(50):
        Thread(target=getApiKey,args=(lock,appFile)).start()