# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from lib.flickrApi.userInformation import UserInformation
from time import sleep
from lib.flickrApi.stat import Stat


class UserInformationThread(Thread):
    def __init__(self, uid, app, writeQueue):
        Thread.__init__(self)
        self.uid = uid
        self.app = app
        self.writeQueue = writeQueue
        self.stat = True

    def run(self):
        if self.stat == True:
            userInfo = UserInformation(self.uid)
            self.userInfo = userInfo.getUserInformation(self.app)
            self.stat = userInfo.getStat()
            if self.userInfo:
                self.writeQueue.put(self.userInfo)
            else:
                print "Try Again In UserInformationThread uid:%s " % self.uid
                self.run()
        else:
            self.stat = Stat.get_stat()
            while self.stat == False:
                sleep(600)
                self.stat = Stat.get_stat()
            self.run()


if __name__ == '__main__':
    pass
