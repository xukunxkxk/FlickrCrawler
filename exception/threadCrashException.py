# __author__=xk
# -*- coding: utf-8 -*-

class ThreadCrashExcetpion(Exception):
    def __init__(self, errMsg=""):
        super(ThreadCrashExcetpion, self).__init__()
        self.msg = errMsg

class DataThreadCrashExcetpion(ThreadCrashExcetpion):
    def __init__(self, errMsg=""):
        super(DataThreadCrashExcetpion, self).__init__()

class ReadingThreadCrashExcetpion(ThreadCrashExcetpion):
    def __init__(self, errMsg=""):
        super(ReadingThreadCrashExcetpion, self).__init__()

class WritingThreadCrashExcetpion(ThreadCrashExcetpion):
    def __init__(self, errMsg=""):
        super(WritingThreadCrashExcetpion, self).__init__()

class SpiderThreadCrashException(ThreadCrashExcetpion):
    def __init__(self, errMsg=""):
        super(SpiderThreadCrashException, self).__init__()

class LoggingThreadCrashException(ThreadCrashExcetpion):
    def __init__(self):
        super(LoggingThreadCrashException, self).__init__()

class DataPoolThreadCrashException(ThreadCrashExcetpion):
    def __init__(self):
        super(DataPoolThreadCrashException, self).__init__()

if __name__ == '__main__':
    pass