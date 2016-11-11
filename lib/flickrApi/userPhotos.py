# __author__=xk
# -*- coding: utf-8 -*-



if __name__ == '__main__':
    pass# __author__=xk
# -*- coding: utf-8 -*-
# from urllib import urlopen
from urllib2 import HTTPError,urlopen
from bs4 import BeautifulSoup
from res.myApp import MyApp
from entity.userPhotosEntity import UserPhotosEntity
from tools.myRequest import Requests
import urllib2

class UserPhotos:
    host="https://api.flickr.com/services/rest/?"
    api="flickr.people.getPublicPhotos"
    def __init__(self, uid):
        self.uid = uid
        self.userPhotosEnity = UserPhotosEntity(uid)
        self.request = Requests()
        self.stat = True
        self.pageCount=0
        self.total = 0

    #返回UserFollowersEntity
    def getPhotos(self, app):
        page = '1'
        api_key = app.getApikey()
        isWrong=False
        try:
            URL = self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid + '&per_page=500' + "&page=" + page
            self.request.get(URL)

            self.pageCount = int(self.request.getAttrsValue('photos', 'pages'))
            self.total = int(self.request.getAttrsValue('photos', 'total'))
            self.stat = str(self.request.getAttrsValue('rsp', 'stat'))
            if self.stat == 'ok':
                if self.total :
                    photoIdList = []
                    downLoadList = []
            while 1:
                if int(page) < self.pageCount:
                    page = str(int(page) + 1)
                    api_key = app.getApikey()
                    self.html = urlopen(self.host + "&method=" + self.api + "&api_key=" + api_key + \
                                         "&user_id=" + self.uid + "&page=" + page)
                    self.returnData = BeautifulSoup(self.html, "html.parser")
                else:
                    break
        except AttributeError as e:
            pass

        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False

        if isWrong==False:
            return self.userPhotosEnity
        else :
            return None




if __name__ == '__main__':
    u=UserPhotos("95200220@N03")
    app=MyApp()
    u.getPhotos(app)




























