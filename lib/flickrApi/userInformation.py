# __author__=xk
# -*- coding: utf-8 -*-
import sys
from urllib2 import HTTPError, urlopen

from bs4 import BeautifulSoup
from entity.userEntity import UserEntity, UserEntity2

from lib.flickrApi.abstractApi.flickrUserApi import FlickrUserApi


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


class UserInformation2(FlickrUserApi):
    def __init__(self, app, uid):
        super(UserInformation2, self).__init__(app, uid)
        self.api = "flickr.people.getInfo"
        self.entity = UserEntity2(uid)

    def analyze(self):
        reload(sys)
        sys.setdefaultencoding('utf8')

        try:
            username = str(self.request.getText("username"))
            if username:
                self.entity.setValue(username = username)
            #用户名不存在逻辑错误，被封号
            else:
                self.entity = None
                return
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            username = str(self.request.getText("username"))
            if username:
                self.entity.setValue(username = username)
            else:
                self.entity = None
                return

        try:
            realname = str(self.request.getText("realname"))
            if realname:
                self.entity.setValue(realname=realname)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            realname = str(self.request.getText("realname"))
            if realname:
                self.entity.setValue(realname=realname)


        try:
            location = str(self.request.getText("location"))
            if location:
                self.entity.setValue(location=location)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            location = str(self.request.getText("location"))
            if location:
                self.entity.setValue(location=location)

        try:
            photosurl = str(self.request.getText("photosurl"))
            if photosurl:
                self.entity.setValue(photosurl=photosurl)
        except AttributeError:
            pass

        try:
            profileurl = str(self.request.getText("profileurl"))
            if profileurl:
                self.entity.setValue(profileurl=profileurl)
        except AttributeError:
            pass

        try:
            firstdatetaken = str(self.request.getText("firstdatetaken"))
            if firstdatetaken != '':
                self.entity.setValue(firstdatetaken=firstdatetaken)
        except AttributeError:
            pass

        try:
            photocount = int(self.request.getText("count"))
            if photocount:
                self.entity.setValue(photocount=photocount)
        except AttributeError:
            pass

if __name__ == '__main__':
    from tools.myApp import MyApp

    app = MyApp()
    userInfo = UserInformation2(app, "100000122@N08")
    entity = userInfo.work()
    print entity.getValue()
    # print entity
    # from db.dbConnect import dbConnect
    #
    # conn, cur = dbConnect()
    # cur.execute("SET CHARSET utf8mb4")
    # cur.execute(
    #     "UPDATE user SET username=%s,realname=%s,location=%s,photosurl=%s,profileurl=%s,photocount=%s,firstdatetaken=%s WHERE uid=%s ",
    #     entity)
    # conn.commit()
    # cur.close()
    # conn.close()
