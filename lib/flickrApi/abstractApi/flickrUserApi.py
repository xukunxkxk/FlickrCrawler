# __author__=xk
# -*- coding: utf-8 -*-
from flickrApi import FlickrApi

class FlickrUserApi(FlickrApi):
    def __init__(self, app, uid):
        super(FlickrUserApi, self).__init__(app)
        self.uid = uid

    def getAddress(self):
        #从app申请apikey
        api_key = self.app.getApikey()
        return self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.uid

if __name__ == '__main__':
    pass