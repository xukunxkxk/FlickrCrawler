# __author__=xk
# -*- coding: utf-8 -*-

class Entity(object):
    def __init__(self):
        self.values = {}
        self.filedName = None
        self.filedSize = 0

    def setValue(self, **kwargs):
        for key in kwargs:
            if not key in self.filedName:
                raise Exception("not defined key keyname = %s" % key)
            self.values[key] = kwargs[key]

    def getValue(self):
        return self.values

    def getFiledName(self):
        return self.filedName

    def getFiledSize(self):
        return self.filedSize

    def setFiledInitValues(self, *values):
        for index in xrange(0, self.filedSize):
            self.values[self.filedName[index]] = values[index]

    def getId(self):
        pass

    def rules(self):
        return True

    def getWritingTakeIdName(self):
        pass





if __name__ == '__main__':
    pass