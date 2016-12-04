# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from lib.flickrApi.userFollowers import UserFollower
from time import sleep


class UserFollowersThread(Thread):
    def __init__(self, uid, app, writeQueue):
        Thread.__init__(self)
        self.uid = uid
        self.app = app
        self.writeQueue = writeQueue

    def run(self):
        self.userFollowers = UserFollower(self.uid).getFollower(self.app)
        if self.userFollowers:
            self.writeQueue.put(self.userFollowers)
        else:
            print "Try Again In UserFollowersThread uid:%s " % self.uid
            self.run()


if __name__ == '__main__':
    pass
