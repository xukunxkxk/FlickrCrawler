# __author__=xk
# -*- coding: utf-8 -*-
from lib.flickr_api.abstract_api.flickr_user_api import FlickrUserApi

class UserPhotos(FlickrUserApi):
    def __init__(self):
        super(UserPhotos, self).__init__()
        self.api = "flickr.people.getPublicPhotos"

    def getAddress(self):
        return super(UserPhotos, self).getAddress() + '&per_page=100'

    def analyze(self):
        try:
            total = int(self.request.getAttrsValue('photos', 'total'))
            if total > 0:
                photoid = self.request.getAllAttrsValue("photo", "id")
                self.entity.setValue(photoid=photoid)
            else:
                self.entity = None
        except AttributeError as e:
            self.stat = False
            return


if __name__ == '__main__':
    from tools.my_app import MyApp
    app = MyApp()
    u = UserPhotos()
    u.setApp(app)
    u.setTaskId("27743519@N00")
    e = u.work()
    print e.getValue()

