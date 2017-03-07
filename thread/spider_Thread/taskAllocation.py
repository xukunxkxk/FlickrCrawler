# __author__=xk
# -*- coding: utf-8 -*-
from spiderThread import *
from tools.myApp import MyApp

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
        if self.api == self.APILIST[0]:
            UserFollowerThread(self.app, self, self.entityQueue).start()
        elif self.api == self.APILIST[1]:
            UserInformationThread(self.app, self, self.entityQueue).start()
        elif self.api == self.APILIST[2]:
            UserPhotosThread(self.app, self, self.entityQueue).start()
        elif self.api == self.APILIST[3]:
            PhotoInformationThread(self.app, self, self.entityQueue).start()
        elif self.api == self.APILIST[4]:
            PhotoUrlThread(self.app, self, self.entityQueue).start()

    def getTask(self):
        return self.readQueue.get()

    def getApp(self):
        return  self.app





if __name__ == '__main__':
    pass