# __author__=xk
# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


class IpLimitedDectedThread(Thread):
    def __init__(self, ipLimited):
        Thread.__init__(self)
        self.ipLimited = ipLimited

    def run(self):
        try:
            while True:
                if (self.ipLimited.test()):
                    sleep(60)
                else:
                    sleep(300)
        except Exception as e:
            self.run()


if __name__ == '__main__':
    pass
