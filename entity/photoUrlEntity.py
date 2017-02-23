# __author__=xk
# -*- coding: utf-8 -*-
class PhotoUrlEntity:
    def __init__(self, photoId):
        self.photoId = photoId
        self.url = None

    def getPhotoId(self):
        return self.photoId

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url


if __name__ == '__main__':
    pass
