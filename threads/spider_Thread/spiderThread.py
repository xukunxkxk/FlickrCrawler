# __author__=xk
# -*- coding: utf-8 -*-
from abstractSpiderThread import AbstractSpiderThread


class UserFollowerThread(AbstractSpiderThread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(UserFollowerThread, self).__init__(app, taskAllocation, entityQueue)

class UserInformationThread(AbstractSpiderThread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(UserInformationThread, self).__init__(app, taskAllocation, entityQueue)

class UserPhotosThread(AbstractSpiderThread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(UserPhotosThread, self).__init__(app, taskAllocation, entityQueue)

class PhotoInformationThread(AbstractSpiderThread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(PhotoInformationThread, self).__init__(app, taskAllocation, entityQueue)

class PhotoUrlThread(AbstractSpiderThread):
    def __init__(self, app, taskAllocation, entityQueue):
        super(PhotoUrlThread, self).__init__(app, taskAllocation, entityQueue)


if __name__ == '__main__':
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    from Queue import Queue
    from taskAllocation import TaskAllocation
    readQueue = Queue()
    entityQueue = Queue()
    readQueue.put("10001104@N00")
    readQueue.put("aaa")
    readQueue.put("10001643@N00")
    readQueue.put("267462045")
    readQueue.put("96452426")
    readQueue.put("258219837")
    taskAllocation = TaskAllocation()
    taskAllocation.setApi("photoInformation")
    taskAllocation.setReadQueue(readQueue)
    taskAllocation.setEntityQueue(entityQueue)
    taskAllocation.allocate()
    while True:
        entity = taskAllocation.entityQueue.get()
        print entity.getValue()
