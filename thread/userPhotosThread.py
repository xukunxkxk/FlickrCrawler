# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from lib.flickrApi.userPhotos import UserPhotos
from time import sleep
from lib.flickrApi.stat import Stat

class UserPhotosThread(Thread):
    def __init__(self, uid, app, writeQueue):
        Thread.__init__(self)
        self.uid = uid
        self.app = app
        self.writeQueue = writeQueue
        self.stat = True

    def run(self):
        if self.stat == True:
            userPhotos = UserPhotos(self.uid)
            userExisit, self.userPhotos = userPhotos.getPhotos(self.app)
            self.stat = userPhotos.getStat()
            if self.userPhotos:
                self.writeQueue.put(self.userPhotos)
            elif userExisit :
                print "Try Again In UserPhotosThread uid: %s " % self.uid
                self.run()
        else:
            self.stat = Stat.get_stat()
            while self.stat == False:
                sleep(600)
                self.stat = Stat.get_stat()
            self.run()
if __name__ == '__main__':
    pass