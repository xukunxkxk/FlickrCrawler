# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from lib.flickrApi.photoInformation import PhotoInformation
from time import sleep
from lib.flickrApi.stat import Stat


class PhotoInformationThread(Thread):
    def __init__(self, photoid, app, writeQueue):
        Thread.__init__(self)
        self.photoid = photoid
        self.app = app
        self.writeQueue = writeQueue
        self.stat = True

    def run(self):
        if self.stat == True:
            photoInformation = PhotoInformation(self.photoid)
            self.photoInfo = photoInformation.getPhotoInformation(self.app)
            self.stat = photoInformation.getStat()
            if self.photoInfo:
                self.writeQueue.put(self.photoInfo)
            else:
                print "Try Again In PhotoInformationThread photoid: %s " % self.photoid
                self.run()
        else:
            self.stat = Stat.get_stat()
            while self.stat == False:
                sleep(600)
                self.stat = Stat.get_stat()
            self.run()


if __name__ == '__main__':
    pass
