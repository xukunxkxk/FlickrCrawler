# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.dbConnect import dbConnect


def tableCreate():
    try:
        conn, cur = dbConnect()
        # table users
        # auto_increment 自增长第一个为起始值第二个为增长量
        cur.execute("CREATE TABLE IF NOT EXISTS users(\
                    id INT  AUTO_INCREMENT KEY,\
                    uid VARCHAR(255) NOT NULL ,\
                    username VARCHAR(255),\
                    realname VARCHAR(255),\
                    location VARCHAR(255),\
                    photosurl VARCHAR(255),\
                    profileurl VARCHAR(255),\
                    photocount INT DEFAULT 0,\
                    firstdatetaken DATETIME,\
                    flag TINYINT NOT NULL DEFAULT 0)")
        cur.execute("CREATE UNIQUE INDEX uid ON users(uid)")

        # table userfollowers
        cur.execute("CREATE TABLE IF NOT EXISTS userfollowers(\
                    id INT AUTO_INCREMENT KEY,\
                    uid VARCHAR(255) NOT NULL,\
                    follower VARCHAR(255) NOT NULL )")
        cur.execute("CREATE UNIQUE INDEX uid ON userfollowers(uid,follower)")

        print "User Table Created Successfully"
        print "Userfollowers Table Created Successfully"

        conn.commit()
        cur.close()
        conn.close()
        # cur.execute("CREATE TABLE IF NOT EXISTS test(id int)")
    except MySQLdb.Error as e:
        print e


if __name__ == '__main__':
    tableCreate()
