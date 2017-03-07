# __author__=xk
# -*- coding: utf-8 -*-

class DBEmptyException(Exception):
    def __init__(self, errMsg=""):
        super(DBEmptyException, self).__init__()
        self.msg = errMsg

if __name__ == '__main__':
    pass