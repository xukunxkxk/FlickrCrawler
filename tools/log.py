# __author__=xk
# -*- coding: utf-8 -*-
from time import ctime, time, localtime, strftime
from myException.ipLimitException import IpLimitException
from time import sleep
from bs4 import BeautifulSoup
from urllib import urlopen
from urllib2 import HTTPError

import re


class Log:
    def __init__(self):
        self.filePath = r'C:\Users\xk\PycharmProjects\Coding\res\log\log' + strftime("%d-%H-%M-%S", localtime())
        self.logFile = open(self.filePath, 'w')
        self.logFile.write(
            '------------------------------------------------------------------------------------------------------------------------------------------------------------------' + '\n')
        self.startTime = ctime()
        self.startTimeSecond = time()
        self.logFile.write('Program Started at ' + str(self.startTime) + '\n')
        self.logFile.flush()
        self.lineCount = 2
        self.limit = 0
        self.statTryCount = 0

    # 判断Flickr是否封了ip
    def isIpLimit(self):
        pattern = re.compile(r"\*\*\*")
        flagCount = 0
        checkFile = open(self.filePath, 'r')
        lines = checkFile.readlines()
        for line in lines:
            m = pattern.match(line)
            if m is not None:
                flagCount += 1
                if flagCount >= 100:
                    if not self.get_stat():
                        print "Flickr Has Limited Your Ip"
                        self.limit = 1
                    else:
                        break
            else:
                flagCount = 0

    def get_stat(self):
        host = "https://api.flickr.com/services/rest/?"
        api = "flickr.contacts.getPublicList"
        uid = "95200220@N03"
        page = '1'
        api_key = "b08c387d713a1ec32b6e22afb455ea56"
        isWrong = False
        try:
            self.statTryCount += 1
            html = urlopen(host + "&method=" + api + "&api_key=" + api_key + \
                           "&user_id=" + uid + "&page=" + page)
            returnData = BeautifulSoup(html, "html.parser")
            stat = str(returnData.find("rsp").attrs["stat"])
            if stat == 'ok':
                return True
        except AttributeError as e:
            return False
        except (HTTPError, IOError) as e:
            if self.statTryCount < 3:
                return self.get_stat()
            else:
                return False

    def writeLog(self, logText):
        try:
            if self.lineCount < 10002:
                perSecond = str((self.lineCount - 2) / (time() - self.startTimeSecond))
                self.logFile.write(logText + ' at ' + str(ctime()) + ' And Had Completed ' + str(
                    self.lineCount - 2) + ' Uids' + ' ' + perSecond + ' PerSecond' + '\n')
                self.lineCount = self.lineCount + 1
                self.logFile.flush()
            else:
                self.isIpLimit()
                self.logFile.close()
                self.filePath = r'C:\Users\xk\PycharmProjects\Coding\res\log\log' + strftime("%d-%H-%M-%S", localtime())
                self.startTimeSecond = time()
                sleep(0.1)
                self.logFile = open(self.filePath, 'w')
                self.logFile.write(
                    '------------------------------------------------------------------------------------------------------------------------------------------------------------------' + '\n')
                self.logFile.flush()
                self.lineCount = 2
                self.writeLog(logText)
        except IOError as e:
            print e
            self.logFile.flush()
            self.writeLog(logText)

            # def  endOfLogging(self):
            #     self.logFile.flush()
            #     self.logFile.write('Programm Ended at ' + str(ctime()) + '\n')
            #     self.logFile.write('From '+str(self.startTime)+' To ' + str(ctime()) +' Written '+' '+str(self.lineCount)+'Uids'+ '\n')


if __name__ == '__main__':
    myLog = Log()
    print myLog.get_stat()
