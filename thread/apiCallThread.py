# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep

from apiThread.photoInformationThread import PhotoInformationThread
from apiThread.userFollowersThread import UserFollowersThread
from apiThread.userInformationThread import UserInformationThread
from apiThread.userPhotosThread import UserPhotosThread


class ApiCallThread(Thread):
    APILIST = ["userFollowers", "userInformation", "userPhotos", "photoInformation"]

    def __init__(self, readQueue, writeQueue, api, app):
        Thread.__init__(self)
        self.api = api
        self.app = app
        self.uid = ""
        self.photoid = ""
        self.readQueue = readQueue
        self.writeQueue = writeQueue

    def apiCalled(self):
        if self.api == self.APILIST[0]:
            self.uid = self.readQueue.get()
            t = UserFollowersThread(self.uid, self.app, self.writeQueue)
            try:
                t.start()
                t.join()
            except Exception as e:
                print e
                sleep(1)
                self.apiCalled()
                # t.start()
                # t.join()

        elif self.api == self.APILIST[1]:
            self.uid = self.readQueue.get()
            t = UserInformationThread(self.uid, self.app, self.writeQueue)
            try:
                t.start()
                t.join()
            except Exception as e:
                print e
                sleep(1)
                self.apiCalled()

        elif self.api == self.APILIST[2]:
            self.uid = self.readQueue.get()
            t = UserPhotosThread(self.uid, self.app, self.writeQueue)
            try:
                t.start()
                t.join()
            except Exception as e:
                print e
                sleep(1)
                self.apiCalled()

        elif self.api == self.APILIST[3]:
            self.photoid = self.readQueue.get()
            t = PhotoInformationThread(self.photoid, self.app, self.writeQueue)
            try:
                t.start()
                t.join()
            except Exception as e:
                print e
                sleep(1)
                self.apiCalled()

        else:
            print self.api
            print "API NOT CODING YET"

    def run(self):
        while 1:
            try:
                self.apiCalled()
                sleep(1)
            except Exception as e:
                print e, " Happened In ApiCalledThread!"
                sleep(1)


if __name__ == '__main__':
    from Queue import Queue
    from tools.myApp import MyApp

    api = "userFollowers"
    readQueue = Queue()
    writeQueue = Queue()
    app = MyApp()
    readQueue.put("95200220@N03")
    readQueue.put("41585601@N05")
    readQueue.put("43496939@N00")
    th = []
    for i in range(3):
        th.append(ApiCallThread(readQueue, writeQueue, api, app))
    for i in th:
        i.start()
    for i in th:
        i.join()
    for i in writeQueue.get():
        print i
    print "---------------------------------------------------------------------------------"

    for i in writeQueue.get():
        print i
    print "---------------------------------------------------------------------------------"

    for i in writeQueue.get():
        print i
