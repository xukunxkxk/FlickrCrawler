# __author__=xk
# -*- coding: utf-8 -*-
class UserPhotosEntity:
    def __init__(self,uid):
        self.uid=uid
        self.photosIdList=list()
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


if __name__ == '__main__':
    pass


