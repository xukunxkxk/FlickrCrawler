# __author__=xk
# -*- coding: utf-8 -*-
from flickrApi import FlickrApi

class FlickrPhotoApi(FlickrApi):
    def __init__(self, app, photoid):
        super(FlickrPhotoApi, self).__init__(app)
        self.photoid = photoid

    def getAddress(self):
        #从app申请apikey
        api_key = self.app.getApikey()
        return self.host + "&method=" + self.api + "&api_key=" + api_key + "&photo_id=" + self.photoid


if __name__ == '__main__':
    pass