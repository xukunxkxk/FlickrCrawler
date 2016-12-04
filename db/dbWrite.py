# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from entity.userFollowersEntity import UserFollowersEntity
from entity.userEntity import UserEntity
from entity.userPhotosEntity import UserPhotosEntity
from entity.photoSizeEntity import PhotoSizeEntity

from res.log import Log
from threading import Thread


def group(uid):
    if uid == '':
        return None
    try:
        return int(uid[-1:])
    except IndexError as e:
        return int(uid[-1:])


class DBWrite:
    def __init__(self, writeQueue, logQueue, conn, cur):
        self.writeQueue = writeQueue
        self.logQueue = logQueue
        self.conn = conn
        self.cur = cur
        self.length = writeQueue.qsize()
        # self.log = Log()

    def setDBConn(self, conn):
        self.conn = conn

    def setDBcur(self, cur):
        self.cur = cur

    def writeDB(self):
        # data=self.writeQueue.get()
        #
        # #userFollower
        # if isinstance(data,UserFollowersEntity):
        #     uid=data.getUid()
        #     size=data.getFollowersSize()
        #     g = group(uid)
        #     try:
        #         #把用户粉丝关系写入数据库
        #         if size:
        #             for follower in data:
        #                 self.cur.execute("INSERT INTO userFollowers(uid,follower) VALUES(%s,%s)",(uid,follower))
        #             s="UPDATE users_"+g+" SET flag=1 WHERE uid=(%s)"
        #             #self.cur.execute("UPDATE users SET flag=1 WHERE uid=(%s)", (uid,))
        #             self.cur.execute(s, (uid,))
        #             print "Uid:%s Followers Writes Finished" % uid
        #         else:
        #             s = "UPDATE users_" + g + " SET flag=1 WHERE uid=(%s)"
        #             self.cur.execute(s, (uid,))
        #     except MySQLdb.IntegrityError as e:
        #         s = "UPDATE users_" + g + " SET flag=1 WHERE uid=(%s)"
        #         # self.cur.execute("UPDATE users SET flag=1 WHERE uid=(%s)", (uid,))
        #         self.cur.execute(s, (uid,))
        #     #更新user
        #
        #     if size:
        #         followerList=[]
        #         for i in range(9):
        #             followerList.append([])
        #         for follower in data:
        #                 g = int(group(follower))
        #                 followerList[g].append((follower,))
        #                 #self.cur.execute("INSERT  INTO users(uid) VALUES(%s)", (follower,))
        #         for i in range(9):
        #             try:
        #                 s = "INSERT INTO users_" + str(i) + "(uid) VALUES(%s)"
        #                 self.cur.executemany(s, followerList[i])
        #             except MySQLdb.Error as e:
        #                 pass
        #
        #     else:
        #         print "Uid %s Didn't have followers"%uid
        #     print "Updated User Finished"
        #     self.conn.commit()
        # maxSQLLength = 10
        maxSQLLength = 1
        data = []
        for i in range(maxSQLLength):
            data.append(self.writeQueue.get())
        # userFollower
        if isinstance(data[0], UserFollowersEntity):
            uid = []
            size = []
            g = []
            argsList = []
            for i in range(maxSQLLength):
                uid.append(data[i].getUid())
                size.append(data[i].getFollowersSize())
                g.append(group(uid[i]))
                if size[i]:
                    for dataFollower in data[i]:
                        argsList.append((uid[i], dataFollower))
            # 写入follower
            try:
                self.cur.executemany("INSERT IGNORE INTO userFollowers(uid,follower) VALUES(%s,%s)", argsList)
                # OperationalError: (2013, 'Lost connection to MySQL server during query')
            except MySQLdb.IntegrityError as e:
                pass
            except MySQLdb.OperationalError as e:  # 太长无法插入
                print e
                try:
                    for i in range(maxSQLLength):
                        errorArgList = []
                        if size[i]:
                            for dataFollower in data[i]:
                                errorArgList.append((uid[i], dataFollower))
                            self.cur.executemany("INSERT IGNORE INTO userFollowers(uid,follower) VALUES(%s,%s)",
                                                 errorArgList)
                except MySQLdb.OperationalError as e:
                    for i in range(maxSQLLength):
                        if size[i]:
                            for dataFollower in data[i]:
                                self.cur.execute("INSERT IGNORE INTO userFollowers(uid,follower) VALUES(%s,%s)",
                                                 (uid[i], dataFollower))

            for i in range(maxSQLLength):
                try:
                    s = "UPDATE users_" + str(g[i]) + " SET flag=1 WHERE uid=(%s)"
                    self.cur.execute(s, (uid[i],))
                    # print "Uid:%s Followers Writes Finished" % uid[i]
                    # self.log.writeLog("Uid:%s Followers Writes Finished" % uid[i])
                except MySQLdb.Error as e:
                    # self.log.writeLog(e)
                    pass

            # 更新user
            followerList = []
            for i in range(9):
                followerList.append([])
            for i in range(maxSQLLength):
                if size[i]:
                    for follower in data[i]:
                        try:
                            g = group(follower)
                            followerList[g].append((follower,))
                        except TypeError:
                            pass
            for i in range(9):
                try:
                    s = "INSERT INTO users_" + str(i) + "(uid) VALUES(%s)"
                    if len(followerList[i]) != 0:
                        self.cur.executemany(s, followerList[i])
                except MySQLdb.Error as e:
                    pass
                except MySQLdb.OperationalError as e:
                    if len(followerList[i]) != 0:
                        for dataFollower in followerList[i]:
                            try:
                                s = "INSERT INTO users_" + str(i) + "(uid) VALUES(%s)"
                                self.cur.execute(s, dataFollower)
                            except MySQLdb.Error as e:
                                pass

            for i in range(maxSQLLength):
                if size[i]:
                    print "Updated UserFollower Uid:%s Finished" % uid[i]
                    # self.log.writeLog("Updated UserFollower Uid:%s Finished" % uid[i])
                    self.logQueue.put("Updated UserFollower Uid:%s Finished" % uid[i])
                else:
                    print "Uid %s Didn't have followers" % uid[i]
                    # self.log.writeLog("Uid %s Didn't have followers" % uid[i])
                    self.logQueue.put("***Uid %s Didn't have followers" % uid[i])
            self.conn.commit()

        # userInformation
        elif isinstance(data[0], UserEntity):
            # uid = data[0].getUid()
            # groupNum = group(uid)
            # groupString = "users_" + str(groupNum)
            # try:
            #     self.cur.execute("SET CHARSET utf8mb4")
            #     query = "UPDATE "+ groupString + " SET username=%s,realname=%s,location=%s,photosurl=%s,profileurl=%s,photocount=%s,firstdatetaken=%s,flag=0 WHERE uid=%s "
            #     self.cur.execute(query,data[0].getValue())
            #     self.conn.commit()
            # except MySQLdb.Error as e:
            #     self.logQueue.put("***"+data[0].getUid()+str(e))
            #     self.cur.execute("SET CHARSET utf8mb4")
            #     if data[0].getValue()[0]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET username=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[0],data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[0] + str(e))
            #     if data[0].getValue()[1]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET realname=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[1],data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[1] + str(e))
            #     if data[0].getValue()[2]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET location=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[2],data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[2] + str(e))
            #     if data[0].getValue()[3]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET photosurl=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[3], data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[3] + str(e))
            #     if data[0].getValue()[4]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET profileurl=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[4], data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[4] + str(e))
            #     if data[0].getValue()[5]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET photocount=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query, (data[0].getValue()[5], data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[5] + str(e))
            #     if data[0].getValue()[6]:
            #         try:
            #             query = "UPDATE " + groupString
            #             query += " SET firstdatetaken=%s,flag=0 WHERE uid=%s "
            #             self.cur.execute(query,(data[0].getValue()[6], data[0].getUid()))
            #         except MySQLdb.Error as e:
            #             self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[6] + str(e))
            #     self.conn.commit()
            #
            # else:
            #     if data[0].username:
            #         print "User uid:%s Information Has Been Updated " % data[0].getUid()
            #         self.logQueue.put("User uid:%s Information Has Been Updated " % data[0].getUid())
            #     else:
            #         print "Wrong in uid:%s " % data[0].getUid()
            #         self.logQueue.put("***Wrong in uid:%s " % data[0].getUid())



            # 返回错误用户
            try:
                self.cur.execute("SET CHARSET utf8mb4")
                self.cur.execute(
                    "UPDATE users_8 SET username=%s,realname=%s,location=%s,photosurl=%s,profileurl=%s,photocount=%s,firstdatetaken=%s,flag=0 WHERE uid=%s ",
                    data[0].getValue())
                self.conn.commit()
            except MySQLdb.Error as e:
                self.logQueue.put("***" + data[0].getUid() + str(e))
                self.cur.execute("SET CHARSET utf8mb4")
                if data[0].getValue()[0]:
                    try:
                        self.cur.execute("UPDATE users_8 SET username=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[0], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[0] + str(e))
                if data[0].getValue()[1]:
                    try:
                        self.cur.execute("UPDATE users_8 SET realname=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[1], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[1] + str(e))
                if data[0].getValue()[2]:
                    try:
                        self.cur.execute("UPDATE users_8 SET location=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[2], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[2] + str(e))
                if data[0].getValue()[3]:
                    try:
                        self.cur.execute("UPDATE users_8 SET photosurl=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[3], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[3] + str(e))
                if data[0].getValue()[4]:
                    try:
                        self.cur.execute("UPDATE users_8 SET profileurl=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[4], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[4] + str(e))
                if data[0].getValue()[5]:
                    try:
                        self.cur.execute("UPDATE users_8 SET photocount=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[5], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[5] + str(e))
                if data[0].getValue()[6]:
                    try:
                        self.cur.execute("UPDATE users_8 SET firstdatetaken=%s,flag=0 WHERE uid=%s ",
                                         (data[0].getValue()[6], data[0].getUid()))
                    except MySQLdb.Error as e:
                        self.logQueue.put("***" + data[0].getUid() + data[0].getValue()[6] + str(e))
                self.conn.commit()

            else:
                if data[0].username:
                    print "User uid:%s Information Has Been Updated " % data[0].getUid()
                    self.logQueue.put("User uid:%s Information Has Been Updated " % data[0].getUid())
                else:
                    print "Wrong in uid:%s " % data[0].getUid()
                    self.logQueue.put("***Wrong in uid:%s " % data[0].getUid())


        elif isinstance(data[0], UserPhotosEntity):
            # uid = data[0].getUid()
            # photoList = data[0].getPhotoList()
            # length = data[0].getCnt()
            # totalList = []
            # if length:
            #     tableName = "photos_" + str(group(uid))
            #     #tableName = "photos_1"
            #     statement = "insert into " + tableName + " (photoid, owner) values(%s, %s)"
            #     for index in range(length):
            #         totalList.append((uid, photoList[index]))
            #     try:
            #         self.cur.executemany(statement, totalList)
            #     except MySQLdb.IntegrityError as e:
            #         print e
            #     except MySQLdb.Error as e:
            #         print e
            #     print "uid: %s photosid has been completed %s photos writeQueue %s" % (uid, data[0].getCnt(), self.writeQueue.qsize())
            #     self.logQueue.put("uid: %s photosid has been completed" % uid)
            # else:
            #     print "uid: %s did not have photos" % uid
            #     self.logQueue.put("uid: %s did not have photos" % uid )
            # s = "update " + "users_" + str(group(uid)) + " set flag=1 where uid=%s "
            # #self.cur.execute(s, (uid,))
            # self.conn.commit()

            uid = []
            photoList = []
            length = []
            totalList = []
            for i in range(maxSQLLength):
                length.append(data[i].getCnt())
                uid.append((data[i].getUid(),))
                if length[i]:
                    for j in range(length[i]):
                        totalList.append((data[i].getPhotoList()[j], data[i].getUid()))
                    print "uid: %s photosid has been completed %s photos writeQueue %s" % (
                    uid[i][0], data[i].getCnt(), self.writeQueue.qsize())
                    self.logQueue.put("uid: %s photosid has been completed" % uid[i][0])
                else:
                    print "uid: %s did not have photos" % uid[i][0]
                    self.logQueue.put("uid: %s did not have photos" % uid[i][0])

            try:
                tableName = "photos_" + str(group(uid[0][0]))
                statement = "insert into " + tableName + " (photoid, owner) values(%s, %s)"
                self.cur.executemany(statement, totalList)
            except MySQLdb.IntegrityError as e:
                pass
            except MySQLdb.OperationalError as e:  # 太长无法插入
                tableName = "photos_" + str(group(uid[0][0]))
                statement = "insert into " + tableName + " (photoid, owner) values(%s, %s)"
                for i in totalList:
                    self.cur.executemany(statement, i)
            except MySQLdb.Error as e:
                print e
            s = "update " + "users_" + str(group(uid[0][0])) + " set flag=1 where uid=%s "
            self.cur.executemany(s, uid)
            self.conn.commit()

        elif isinstance(data[0], PhotoSizeEntity):
            photoId = data[0].getPhotoId()
            url = data[0].getUrl()
            self.cur.execute("update photos_0 set downloadurl = %s where photoid = %s", (url, photoId))


if __name__ == '__main__':
    from db.dbConnect import dbConnect
    from db.dbRead import DBRead
    from dbClose import dbClose
    from  Queue import Queue
    from res.myApp import MyApp
    from apiCallThread import ApiCallThread

    readQueue = Queue()
    writeQueue = Queue()
    conn, cur = dbConnect()
    app = MyApp()
    dbR = DBRead(readQueue, "userInformation", conn, cur)
    dbW = DBWrite(writeQueue, None, conn, cur)
    dbR.readUid()
    ApiCallThread(readQueue, writeQueue, "userInformation", app).start()
    dbW.writeDB()
    dbClose(conn, cur)
