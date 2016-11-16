# __author__=xk
# -*- coding: utf-8 -*-
from tools import myRequest
from time import ctime
from urllib import urlretrieve
from urllib2 import HTTPError

if __name__ == '__main__':
    ##下载flickr图片
    # request = myRequest.Requests()
    # photourl = raw_input("输入图片地址: ")
    # request.get(photourl)
    # url = 'http:'+ request.getAllAttrsValue("img", "src")[1].split('.jpg')[0] + '_h.jpg'
    # filename ='D:/photos/'+ url.split('/')[5].split('_')[0] + '.jpg'
    # try:
    #     urlretrieve(url, filename)
    # except HTTPError as e:
    #     print e


    from urllib2 import urlopen
    from urllib import urlretrieve
    from bs4 import BeautifulSoup
    import re
    import sys

    # html = urlopen('http://m.youmzi.com/meinv.html')
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # photoid = 12990
    # cnt = 10
    # for i in range(cnt):
    #     print cnt
    #     try:
    #         url = 'http://m.youmzi.com/' + str(photoid) + '.html'
    #         photoid = photoid + 1
    #         html = urlopen(url)
    #         photoname = html.geturl().split('/')[3].split('.')[0] + '.jpg'
    #         bsoj = BeautifulSoup(html, 'html.parser')
    #         l = []
    #         for e in bsoj.findAll('a', {'href': re.compile('.jpg$')}):
    #             l.append(e['href'])
    #         for e in l:
    #             urlretrieve(e, photoname)
    #     except Exception as e:
    #         print e

    a = [1,2,3]
    b = [2,3,4]
    a.extend(b)
    print a
