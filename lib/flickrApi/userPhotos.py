# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError
from res.myApp import MyApp
from entity.userPhotosEntity import UserPhotosEntity
from tools.myRequest import Requests

class UserPhotos:
    host="https://api.flickr.com/services/rest/?"
    api="flickr.people.getPublicPhotos"
    def __init__(self, uid):
        self.uid = uid
        self.userPhotosEnity = UserPhotosEntity(uid)
        self.request = Requests()
        self.photoIdList = []
        self.stat = True
        self.pageCount=0
        self.page = 1
        self.total = 0

    #返回UserFollowersEntity
    def getPhotos(self, app):
        api_key = app.getApikey()
        try:
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid + '&per_page=500' + "&page=" + str(self.page)
            self.request.get(url)
            #判断usersPhotos
            try:
                stat = str(self.request.getAttrsValue('rsp', 'stat'))
                #用户不存在
                if stat == "fail":
                    self.stat = True
                    return self.userPhotosEnity
                #用户存在
                elif stat == "ok":
                    self.stat = True
            except AttributeError as e:
                self.stat = False
                return self.userPhotosEnity
            self.pageCount = int(self.request.getAttrsValue('photos', 'pages'))
            self.total = str(self.request.getAttrsValue('photos', 'total'))
        except TypeError as e:
            return self.userPhotosEnity

        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False
            return None

        if not self.request.getBSObjet():
            return None

        #照片数大于0则加入用户照片list
        if self.total > 0:
            self.userPhotosEnity.extend(self.request.getAllAttrsValue("photo", "id"))

        #照片数多于1页
        while self.page < self.pageCount:
            print self.page
            self.page += 1
            api_key = app.getApikey()
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid + '&per_page=500' + "&page=" + str(self.page)
            error = True
            while error:
                try:
                    self.request.get(url)
                    try:
                        stat = str(self.request.getAttrsValue('rsp', 'stat'))
                        if stat == "ok":
                            self.stat = True
                        elif stat == "false":
                            self.stat = True
                            return self.userPhotosEnity
                    except AttributeError as e:
                        self.stat = False
                        return None
                except (HTTPError, IOError) as e:
                    print e
                    if str(e) == "HTTP Error 429: ":
                        self.stat = False
                else:
                    error = False
            #添加新的photosId
            self.userPhotosEnity.extend(self.request.getAllAttrsValue("photo", "id"))

        print self.userPhotosEnity.getCnt()
        return self.userPhotosEnity

    def getStat(self):
        return self.stat


if __name__ == '__main__':
    u=UserPhotos("27743519@N00")
    app=MyApp()
    usersEntity = u.getPhotos(app)
    for id in  usersEntity.getPhotoList():
        print id
    print usersEntity.getCnt()
    print usersEntity.getUid()
    print u.page





























