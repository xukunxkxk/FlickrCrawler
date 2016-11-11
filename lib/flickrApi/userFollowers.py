# __author__=xk
# -*- coding: utf-8 -*-
# from urllib import urlopen
from urllib2 import HTTPError,urlopen
from bs4 import BeautifulSoup
from res.myApp import MyApp
from entity.userFollowersEntity import UserFollowersEntity

import urllib2

class UserFollower:
    host="https://api.flickr.com/services/rest/?"
    api="flickr.contacts.getPublicList"
    def __init__(self,uid):
        self.uid=uid
        self.userFllowers=UserFollowersEntity(uid)
        self.html=None
        self.returnData=None
        self.pageCount=0

    #返回UserFollowersEntity
    def getFollower(self,app):
        page = '1'
        api_key = app.getApikey()
        isWrong=False
        try:
            self.html = urlopen(self.host + "&method=" + self.api + "&api_key=" + api_key + \
                          "&user_id=" + self.uid + "&page=" + page)
            self.returnData=BeautifulSoup(self.html,"html.parser")
            self.pageCount=int(self.returnData.find("contacts").attrs["pages"])
            while 1:
                for f in self.returnData.findAll("contact"):
                    self.userFllowers.addFollowers(f.attrs["nsid"])
                if int(page)<self.pageCount:
                    page = str(int(page) + 1)
                    api_key = app.getApikey()
                    self.html = urlopen(self.host + "&method=" + self.api + "&api_key=" + api_key + \
                                         "&user_id=" + self.uid + "&page=" + page)
                    self.returnData = BeautifulSoup(self.html, "html.parser")
                else:
                    break
        except AttributeError as e:
            pass
        except (HTTPError,IOError) as e:
            print e
            isWrong=True

        if isWrong==False:
            return self.userFllowers
        else :
            return None




if __name__ == '__main__':
    u=UserFollower("95200220@N03")
    app=MyApp()
    data=u.getFollower(app)
    if data:
        for i in data:
            print i





























