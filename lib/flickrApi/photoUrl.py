# __author__=xk
# -*- coding: utf-8 -*-
from urllib2 import HTTPError
from entity.photoUrlEntity import PhotoUrlEntity
from tools.myApp import MyApp
from tools.myRequest import Requests


class PhotoUrl:
    host = "https://api.flickr.com/services/rest/?"
    api = "flickr.photos.getSizes"

    def __init__(self, photoId):
        self.photoId = photoId
        self.photoSizeEntity = PhotoUrlEntity(photoId)
        self.request = Requests()
        self.stat = True

    # 返回UserFollowersEntity
    def getPhotosUrl(self, app):
        api_key = app.getApikey()
        try:
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&photo_id=" + self.photoId
            self.request.get(url)
            self.stat = str(self.request.getAttrsValue('rsp', 'stat'))
            photoUrlList = []
            photoUrlList = self.request.getAllAttrsValue('size', 'source')
            photoUrl = photoUrlList[len(photoUrlList) - 1]
            self.photoSizeEntity.setUrl(photoUrl)
        except AttributeError as e:
            self.stat = False
            return None
        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False
            return None

        return self.photoSizeEntity

    def getStat(self):
        return self.stat


if __name__ == '__main__':
    u = PhotoUrl("31033031911")
    app = MyApp()
    PhotoSize = u.getPhotosUrl(app)

