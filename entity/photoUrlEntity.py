# __author__=xk
# -*- coding: utf-8 -*-
from baseEntity.abstractPhotoEntity import AbstractPhotoEntity
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


class PhotoUrlEntity2(AbstractPhotoEntity):
    def __init__(self, photoid):
        super(PhotoUrlEntity2, self).__init__(photoid)
        self.filedName = ["downloadurl"]
        self.filedSize = 1
        self.setFiledInitValues(None)

if __name__ == '__main__':
    p = PhotoUrlEntity2("1111")
    print p.getValue()
    print p.getId()
    p.setValue(downloadurl = "ff3r43.com")
    print p.getValue()

