# __author__=xk
# -*- coding: utf-8 -*-

from threads.thread_pool import ThreadPool

if __name__ == '__main__':
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    threadPool = ThreadPool("photos_0")
    threadPool.setApi(4)
    threadPool.init()
    threadPool.start()