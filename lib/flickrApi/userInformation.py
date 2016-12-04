# __author__=xk
# -*- coding: utf-8 -*-
from entity.userEntity import UserEntity
# from urllib import urlopen
from urllib2 import HTTPError, urlopen
from bs4 import BeautifulSoup
import sys
import urllib2


class UserInformation:
    host = "https://api.flickr.com/services/rest/?"
    api = "flickr.people.getInfo"

    def __init__(self, uid):
        self.uid = uid
        self.userEntity = UserEntity(uid)
        self.returnData = None
        self.stat = True

    def getUserInformation(self, app):
        api_key = app.getApikey()
        reload(sys)
        sys.setdefaultencoding('utf8')
        try:
            self.html = urlopen(self.host + "&method=" + self.api + "&api_key=" + api_key + \
                                "&user_id=" + self.uid)
            self.returnData = BeautifulSoup(self.html, "html.parser")
            # 判断是否被封ip
            try:
                self.stat = str(self.returnData.find("rsp").attrs["stat"])
            except AttributeError:
                self.stat = False
        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False

        if not self.returnData:
            return None

        try:
            username = str(self.returnData.find("username").get_text())
            if username:
                self.userEntity.setUsername(username)
            else:
                return None
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            username = str(self.returnData.find("username").get_text())
            if username:
                self.userEntity.setUsername(username)
            else:
                return None

        try:
            realname = str(self.returnData.find("realname").get_text())
            if realname:
                self.userEntity.setRealname(realname)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            realname = str(self.returnData.find("realname").get_text())
            if realname:
                self.userEntity.setRealname(realname)

        try:
            location = str(self.returnData.find("location").get_text())
            if location:
                self.userEntity.setLocation(location)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            location = str(self.returnData.find("location").get_text())
            if location:
                self.userEntity.setLocation(location)

        try:
            photosurl = str(self.returnData.find("photosurl").get_text())
            if photosurl:
                self.userEntity.setPhotosurl(photosurl)
        except AttributeError:
            pass

        try:
            profileurl = str(self.returnData.find("profileurl").get_text())
            if profileurl:
                self.userEntity.setProfileurl(profileurl)
        except AttributeError:
            pass

        try:
            firstdatetaken = str(self.returnData.find("firstdatetaken").get_text())
            if firstdatetaken != '':
                self.userEntity.setFirstdatetaken(firstdatetaken)
        except AttributeError:
            pass

        try:
            count = int(self.returnData.find("count").get_text())
            if count:
                self.userEntity.setPhotocount(count)
        except AttributeError:
            pass

        return self.userEntity

    def getStat(self):
        return self.stat


if __name__ == '__main__':
    from res.myApp import MyApp

    app = MyApp()
    userInfo = UserInformation("100000122@N08")
    entity = userInfo.getUserInformation(app).getValue()
    print entity
    from db.dbConnect import dbConnect

    conn, cur = dbConnect()
    cur.execute("SET CHARSET utf8mb4")
    cur.execute(
        "UPDATE user SET username=%s,realname=%s,location=%s,photosurl=%s,profileurl=%s,photocount=%s,firstdatetaken=%s WHERE uid=%s ",
        entity)
    conn.commit()
    cur.close()
    conn.close()
