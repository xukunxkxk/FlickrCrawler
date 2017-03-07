# __author__=xk
# -*- coding: utf-8 -*-
from lib.flickrApi.abstractApi.flickrPhotoApi import FlickrPhotoApi


class PhotoUrl(FlickrPhotoApi):
    def __init__(self):
        super(PhotoUrl, self).__init__()
        self.api = "flickr.photos.getSizes"

    def analyze(self):
        try:
            photoUrlList = self.request.getAllAttrsValue('size', 'source')
            downloadurl = photoUrlList[len(photoUrlList) - 1]
            self.entity.setValue(downloadurl=downloadurl)
        except AttributeError as e:
            self.stat = False
            return

if __name__ == '__main__':
    from tools.myApp import MyApp
    app = MyApp()
    u = PhotoUrl()
    u.setApp(app)
    u.setTaskId("9461940523")
    entity  = u.work()
    print entity.getValue()

