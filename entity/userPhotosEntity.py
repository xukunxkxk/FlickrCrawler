# __author__=xk
# -*- coding: utf-8 -*-
from baseEntity.abstractUserEntity import AbstractUserEntity
class UserPhotosEntity():
    def __init__(self, uid):
        self.uid = uid
        self.photosIdList = list()
        self.cnt = 0

    def getUid(self):
        return self.uid

    def getPhotoList(self):
        return self.photosIdList

    def getCnt(self):
        return self.cnt

    def add(self, photoId):
        self.photosIdList.append(photoId)
        self.cnt += 1

    def extend(self, photoList):
        self.photosIdList.extend(photoList)
        self.cnt += len(photoList)


class UserPhotosEntity2(AbstractUserEntity):
    def __init__(self, uid):
        super(UserPhotosEntity2, self).__init__(uid)
        self.filedName = ["photoid"]
        self.filedSize = 1
        self.setFiledInitValues(None)

if __name__ == '__main__':
    up = UserPhotosEntity2("aaaa")
    print up.getValue()
    v = ["111","2222"]
    up.setValue(photoid = v)
    print up.getValue()
