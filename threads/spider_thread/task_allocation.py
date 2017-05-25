# __author__=xk
# -*- coding: utf-8 -*-
from spider_thread import *
from tools.my_app import MyApp

class TaskAllocation:
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    def __init__(self):
        self.app = MyApp()
        self.endFlag = False

    def setApi(self, api):
        self.api = api

    def setEntityQueue(self, entityQueue):
        self.entityQueue = entityQueue

    def setReadQueue(self, readQueue):
        self.readQueue = readQueue

    def allocate(self):
        spiderThread = None
        if self.api == self.APILIST[0]:
            spiderThread = UserFollowerThread(self.app, self, self.entityQueue)
        elif self.api == self.APILIST[1]:
            spiderThread = UserInformationThread(self.app, self, self.entityQueue)
        elif self.api == self.APILIST[2]:
            spiderThread = UserPhotosThread(self.app, self, self.entityQueue)
        elif self.api == self.APILIST[3]:
            spiderThread = PhotoInformationThread(self.app, self, self.entityQueue)
        elif self.api == self.APILIST[4]:
            spiderThread = PhotoUrlThread(self.app, self, self.entityQueue)
        spiderThread.start()
        return spiderThread

    def getTask(self):
        return self.readQueue.get()

    def getApp(self):
        return  self.app





if __name__ == '__main__':
    pass