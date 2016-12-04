# __author__=xk
# -*- coding: utf-8 -*-
from tools import myRequest
from tools.myRequest import Requests
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

    # request = Requests()
    # url = "http://tieba.baidu.com/p/4817897515"
    # request.get(url= url)
    # hrefList = request.getAllAttrsValue('img', 'src', regx='\\.jpg$')
    # fileNameList = request.getFileNameList(hrefList, fileDir="D:\photos")
    # request.down(fileNameList, hrefList)

    request = Requests()
    url = "https://www.zhanqi.tv/videos/xindong/2016/11/160065.html"
    request.get("https://www.zhanqi.tv/videos/xindong/2016/11/160065.html")
    print request.getAllAttrsValue("a", "href")
