# __author__=xk
# -*- coding: utf-8 -*-
from  threadGenerator import ThreadGenerator
from time import sleep
import os


if __name__ == '__main__':
    threadGenerator=ThreadGenerator("photoInformation")
    # threadGenerator=ThreadGenerator("photoUrl")
    # threadGenerator.setDaemon(True)
    threadGenerator.start()
    # while 1:
    #     if threadGenerator.logThread.log.limit == 1:
    #         print "Ip Limited Wait For Some Minutes"
    #         os._exit(1)
    #     sleep(10)


