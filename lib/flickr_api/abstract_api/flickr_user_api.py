# __author__=xk
# -*- coding: utf-8 -*-
from flickr_api import AbstractFlickrApi

class FlickrUserApi(AbstractFlickrApi):
    def __init__(self):
        super(FlickrUserApi, self).__init__()

    def getAddress(self):
        #从app申请apikey
        api_key = self.app.getApikey()
        return self.host + "&method=" + self.api + "&api_key=" + api_key + "&user_id=" + self.taskId

if __name__ == '__main__':
    pass