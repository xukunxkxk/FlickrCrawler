# __author__=xk
# -*- coding: utf-8 -*-

class IpLimitedExcetpion(Exception):
    def __init__(self, errMsg=""):
        super(IpLimitedExcetpion, self).__init__()
        self.msg = errMsg

if __name__ == '__main__':
    from time import sleep
    from random import Random
    try:
        for i in xrange(0, 10):
            random = Random()
            if random.randint(0, 2) % 2 == 0:
                raise Exception("Ip limited")
    except Exception as e:
        raise IpLimitedExcetpion("Msg")
    print "res"

