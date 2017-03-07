# __author__=xk
# -*- coding: utf-8 -*-

from threadPool import ThreadPool

if __name__ == '__main__':
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    threadPool = ThreadPool("photos_1_copy")
    threadPool.setApi(4)
    threadPool.init()
    threadPool.start()