# __author__=xk
# -*- coding: utf-8 -*-

from threading import Thread
from lib.flickrApi.photoUrl import PhotoUrl
from time import sleep
from lib.flickrApi.stat import Stat

class PhotoUrlThread(Thread):
    def __init__(self, photoid, app, writeQueue):
        Thread.__init__(self)
        self.photoid = photoid
        self.app = app
        self.writeQueue = writeQueue
        self.stat = True

    def run(self):
        if self.stat == True:
            photoUrl = PhotoUrl(self.photoid)
            self.photoUrl = photoUrl.getPhotosUrl(self.app)
            self.stat = photoUrl.getStat()
            if self.photoUrl:
                self.writeQueue.put(self.photoUrl)
            else:
                print "Try Again In PhotoUrlThread uid:%s " % self.photoid
                self.run()
        else:
            self.stat = Stat.get_stat()
            while self.stat == False:
                sleep(600)
                self.stat = Stat.get_stat()
            self.run()

if __name__ == '__main__':
    pass