# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError

from entity.photoSizeEntity import PhotoSizeEntity
from tools.myApp import MyApp
from tools.myRequest import Requests


class PhotoSize:
    host = "https://api.flickr.com/services/rest/?"
    api = "flickr.photos.getSizes"

    def __init__(self, photoId):
        self.photoId = photoId
        self.photoSizeEntity = PhotoSizeEntity(photoId)
        self.request = Requests()
        self.stat = True

    # 返回UserFollowersEntity
    def getPhotos(self, app):
        api_key = app.getApikey()
        try:
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid + '&per_page=500' + "&page=" + str(
                self.page)
            self.request.get(url)
            self.pageCount = int(self.request.getAttrsValue('photos', 'pages'))
            self.stat = str(self.request.getAttrsValue('rsp', 'stat'))
            self.total = str(self.request.getAttrsValue('photos', 'total'))
        except AttributeError as e:
            self.stat = False
            return None
        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False
            return None

        if not self.request.getBSObjet():
            return None

        # 照片数大于0则加入
        if self.total > 0:
            for id in self.request.getAllAttrsValue("photo", "id"):
                self.userPhotosEnity.add(id)

        # 照片数多于1页
        while self.page < self.pageCount:
            self.page += 1
            api_key = app.getApikey()
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid + '&per_page=500' + "&page=" + str(
                self.page)
            try:
                self.request.get(url)
                self.pageCount = int(self.request.getAttrsValue('photos', 'pages'))
                self.stat = str(self.request.getAttrsValue('rsp', 'stat'))
            except AttributeError as e:
                self.stat = False
                return None
            except (HTTPError, IOError) as e:
                print e
                if str(e) == "HTTP Error 429: ":
                    self.stat = False
                return None
            if not self.request.getBSObjet():
                return None
            for id in self.request.getAllAttrsValue("photo", "id"):
                self.userPhotosEnity.add(id)

        return self.userPhotosEnity

    def getStat(self):
        return self.stat


if __name__ == '__main__':
    u = UserPhotos("10001104@N00")
    app = MyApp()
    usersEntity = u.getPhotos(app)
    for id in usersEntity.getPhotoList():
        print id
    print usersEntity.getCnt()
    print usersEntity.getUid()
    print u.page
