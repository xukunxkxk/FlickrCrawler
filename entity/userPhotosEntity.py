# __author__=xk
# -*- coding: utf-8 -*-
class UserPhotosEntity:
    def __init__(self,uid):
        self.uid=uid
        self.photosIdList=list()
        self.downloadList = list()
        self.photoCnt = 0

    def setPhotos(self, photoList, downloadList):
        self.photosIdList = photoList
        self.downloadList = downloadList
        self.photosCnt = len(self.photosIdList)

    def getUid(self):
        return self.uid

    def getPhotoList(self):
        return self.photosIdList

    def getDownloadList(self):
        return self.downloadList

    def getPhotoCnt(self):
        return self.photoCnt





if __name__ == '__main__':
    pass


