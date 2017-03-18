# __author__=xk
# -*- coding: utf-8 -*-
from threading import Thread
from db.dbConnect import dbConnect
from time import sleep
from db.dbWritingRules.dbWritingRules import *
from exception.threadCrashException import WritingThreadCrashExcetpion
import logging
import logging.config
import os
def group(uid):
    if uid == '':
        return None
    try:
        return int(uid[-1:])
    except IndexError as e:
        return int(uid[-1:])

class WritingThread(Thread):
    APILIST = ["UserFollowers", "UserInformation", "UserPhotos", "PhotoInformation", "PhotoUrl"]
    def __init__(self):
        super(WritingThread, self).__init__()
        self.maxSQLLength = 100
        self.writingDB = None
        self.update = True
        logFilePath = os.path.join(os.path.dirname(__file__), "../../res/logging.conf")
        logging.config.fileConfig(logFilePath)
        self.logger = logging.getLogger("log")

    def run(self):
        self.logger.info("Writing Thread Has been started")
        try:
            self._running()
        except Exception as e:
            self.logger.error(e)
            raise WritingThreadCrashExcetpion("Error: Writing Thread Has Been Crashed!")


    def setTableName(self, tableName):
        self.writingDB.setDBTable(tableName)

    def setApi(self, api):
        self.api = api
        className = api+ "Writing"+"()"
        self.writingDB = eval(className)
        if self.api == self.APILIST[0] or self.api == self.APILIST[2]:
            self.update = False
        # self.writingDB.setFlag(flag="flag", flagValue=0)

    def setWritingQueue(self, writingQueue):
        self.writingQueue = writingQueue

    def _connectDB(self):
        self.conn, self.cur = dbConnect()


    def _writeDB(self):
        entityList = []
        for x in xrange(self.maxSQLLength):
            entityList.append(self.writingQueue.get())
        if self.update:
            self.writingDB.batchUpdate(entityList)
        else:
            self.writingDB.batchInsert(entityList)

    def _running(self):
        while True:
            self._writeDB()
            sleep(1)

    def closeConn(self):
        self.conn.close()
        self.cur.close()

    def getConn(self):
        return self.conn, self.cur

if __name__ == '__main__':
    pass