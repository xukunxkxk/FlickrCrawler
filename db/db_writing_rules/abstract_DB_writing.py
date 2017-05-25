# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.db_connect import dbConnect
import logging
import logging.config
import os

class AbstractDBWriting(object):
    def __init__(self):
        self.fieldName = []
        self.entityValueList = []
        self.task = None
        self._getConnection()
        self.writingCount = 0
        logFilePath = os.path.join(os.path.dirname(__file__), "../../res/logging.conf")
        logging.config.fileConfig(logFilePath)
        self.logger = logging.getLogger("log")

    def setConnection(self, conn, cur):
        self._setConn(conn)
        self._setCur(cur)

    def setDBTable(self, tableName):
        self.tableName = tableName

    def setFlag(self, flagValue=0, flag="flag"):
        self.flag = flag
        self.flagValue =flagValue

    def update(self, entity):
        self._updateEntityCoping(entity)
        self.cur.execute(self.sql, tuple(self.values))
        self.conn.commit()

    def batchUpdate(self, entityList):
        valuesList = []
        for entity in entityList:
            self._updateEntityCoping(entity)
            valuesList.append(self.values)
        try:
            self.cur.executemany(self.sql, valuesList)
        #过长
        except MySQLdb.OperationalError as e:
            self.logger.error(e)
            self._closeConnection()
            self._getConnection()
            for entity in entityList:
                self.update(entity)
            self.conn.commit()
        else:
            self.conn.commit()
        self.writingCount += len(entityList)
        if self.writingCount % 100 == 0:
            self.logger.info("Has Complete %s " % self.writingCount)

    def _updateEntityCoping(self, entity):
        self.values = entity.getValue().values()
        self.id = entity.getId()
        self.values.append(self.id)
        self.fieldName = entity.getValue().keys()
        if self.task == None:
            self.task = entity.getWritingTakeIdName()
            self._updateSQL(self.tableName)

    def _updateSQL(self, tableName):
        sql = "update " + tableName + " " + "set "
        for field in self.fieldName:
            sql += field + "=%s"
            sql += ", "
        sql = sql.strip(", ")
        sql += " where " + self.task + "=%s"
        self.sql = sql

    
    def insert(self, entity):
        self._insertEntityCoping(entity)
        self.cur.execute(self.sql, tuple(self.values))
        self.conn.commit()

    def batchInsert(self, entityList):
        valuesList = []
        for entity in entityList:
            self._insertEntityCoping(entity)
        try:
            self.cur.executemany(self.sql, valuesList)
        #过长插不进去
        except MySQLdb.OperationalError as e:
            self.logger.error(e)
            self._closeConnection()
            self._getConnection()
            for entity in entityList:
                self.insert(entity)
        else:
            self.conn.commit()
        self.writingCount += len(entityList)
        if self.writingCount % 10 == 0:
            self.logger.info("Has Complete %s " % self.writingCount)

    def _insertEntityCoping(self, entity):
        self.values = entity.getValue().values()
        self.id = entity.getId()
        self.values.append(self.id)
        self.fieldName = entity.getValue().keys()
        if self.task == None:
            self.task = entity.getWritingTakeIdName()
            self._insertSQL(self.tableName)

    def _insertSQL(self, tableName):
        sql = "insert into " + tableName + "("
        for field in self.fieldName:
            sql += field + ", "
        sql += self.task
        sql += ") values("
        for field in self.fieldName:
            sql +="%s, "
        sql += "%s) "
        self.sql = sql

    def _setConn(self, conn):
        self.conn = conn

    def _setCur(self, cur):
        self.cur = cur

    def _getConnection(self):
        self.conn, self.cur = dbConnect()

    def _closeConnection(self):
        self.conn.close()
        self.cur.close()

if __name__ == '__main__':
    from entity.flickr_entity import *
    from db.db_connect import dbConnect

    # infoEntity1 = PhotoInformationEntity("1")
    # infoEntity1.setValue(views=1, title=2, comments=5)
    # infoEntity2 = PhotoInformationEntity("347")
    # infoEntity2.setValue(views=1, title=2, comments=5)
    # entityList = [infoEntity1, infoEntity2]
    # ab = AbstractDBWriting()
    # ab.setConnection(conn, cur)
    # ab.setFlag(flag="flag", flagValue=0)
    # ab.setDBTable("photos_1_copy")
    # ab.batchUpdate(entityList)

    ab = AbstractDBWriting()
    ab.setDBTable("photos_1_copy")
    l = []
    for i in xrange(1000000):
        entity = UserPhotosEntity(str(i) + "ww")
        entity.setValue(photoid=str(i) + 'www')
        l.append(entity)
    ab.batchInsert(l)