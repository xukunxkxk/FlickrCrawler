# __author__=xk
# -*- coding: utf-8 -*-
import sys
from urllib2 import HTTPError

from entity.photoEntity import PhotoEntity, PhotoEntity2
from tools.myRequest import Requests
from tools.timeStamp import timestampConvertToTime

from lib.flickrApi.abstractApi.flickrPhotoApi import FlickrPhotoApi

class PhotoInformation:
    host = "https://api.flickr.com/services/rest/?"
    api = "flickr.photos.getInfo"

    def __init__(self, photoid):
        self.photoid = photoid
        self.photoEntity = PhotoEntity(photoid)
        self.request = Requests()
        self.stat = True
        self.sep = ','
        self.views = 0
        self.title = ""
        self.dates = None
        self.comments = ""
        self.tags = ""

    def getPhotoInformation(self, app):
        api_key = app.getApikey()
        reload(sys)
        sys.setdefaultencoding('utf8')

        # 访问api并判断是否被封
        try:
            url = self.host + "&method=" + self.api + "&api_key=" + api_key + "&photo_id=" + self.photoid
            self.request.get(url)
            try:
                stat = str(self.request.getAttrsValue('rsp', 'stat'))
                # 照片不存在
                if stat == "fail":
                    self.stat = True
                    return self.photoEntity
                # 照片存在
                elif stat == "ok":
                    self.stat = True
            except AttributeError as e:
                self.stat = False
                return self.photoEntity
        except TypeError as e:
            return self.photoEntity
        except (HTTPError, IOError) as e:
            print e
            if str(e) == "HTTP Error 429: ":
                self.stat = False
            elif str(e) == r"HTTP Error 418: I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\nHTTP/1.0 418 I'm a teapot (RFC 2324)\r\nExpires: Thu, 01 Jan 1970 22:00:00 GMT\r\nCache-Control: private, no-cache, no-store\r\n\r\n":
                self.stat = False
            return None

        if not self.request.getBSObjet():
            return None

        # views
        try:
            self.views = self.request.getAttrsValue("photo", "views")
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            self.views = self.request.getAttrsValue("photo", "views")

        # titles
        try:
            self.title = self.request.getText("title")
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            self.titles = self.request.getText("title")

        # dates
        try:
            self.dates = self.request.getAttrsValue("dates", "posted")
            self.dates = timestampConvertToTime(self.dates)
        except AttributeError:
            pass

        # comments
        try:
            self.comments = self.request.getText("comments")
        except AttributeError:
            pass

        # tags
        try:
            tagList = self.request.getAllAttrsValue("tag", "raw")
            pre = ""
            for tag in tagList:
                self.tags += tag + ","
                if len(self.tags) > 797:
                    self.tags = pre
                    break
                else:
                    pre = self.tags
            if self.tags == "":
                self.tags = None
            else:
                self.tags = self.tags[0: len(self.tags) - 2]
            if self.tags and len(self.tags ) > 797:
                self.tags = None
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            tagList = self.request.getAllAttrsValue("tag", "raw")
            for tag in tagList:
                self.tags += tag + ","
            if self.tags == "":
                self.tags = None
                print "None"
            else:
                self.tags = self.tags[0: len(self.tags) - 2]

        self.photoEntity.setValue(self.views, self.title, self.dates, self.comments, self.tags)
        return self.photoEntity

    def getStat(self):
        return self.stat

class PhotoInformation2(FlickrPhotoApi):
    def __init__(self, app, photoid):
        super(PhotoInformation2, self).__init__(app, photoid)
        self.api = "flickr.photos.getInfo"
        self.entity = PhotoEntity2(photoid)

    def analyze(self):
        reload(sys)
        sys.setdefaultencoding('utf8')

        if not self.exits:
            return

        # views
        try:
            views = self.request.getAttrsValue("photo", "views")
            self.entity.setValue(views=views)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            views = self.request.getAttrsValue("photo", "views")
            self.entity.setValue(views=views)

        # titles
        try:
            title = self.request.getText("title")
            self.entity.setValue(title=title)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            title = self.request.getText("title")
            self.entity.setValue(title=title)

        # dates
        try:
            dates = self.request.getAttrsValue("dates", "posted")
            dates = timestampConvertToTime(dates)
            self.entity.setValue(dates=dates)
        except AttributeError:
            pass

        # comments
        try:
            comments = self.request.getText("comments")
            self.entity.setValue(comments=comments)
        except AttributeError:
            pass

        # tags
        try:
            tags = ""
            tagList = self.request.getAllAttrsValue("tag", "raw")
            pre = ""
            for tag in tagList:
                tags += tag + ","
                if len(tags) > 797:
                    tags = pre
                    break
                else:
                    pre = tags
            if tags == "":
                tags = None
            else:
                tags = tags[0: len(tags) - 2]
            if tags and len(tags ) > 797:
                tags = None
            self.entity.setValue(tags=tags)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            reload(sys)
            sys.setdefaultencoding('utf8')
            tags = ""
            tagList = self.request.getAllAttrsValue("tag", "raw")
            for tag in tagList:
                tags += tag + ","
            if not tags == "":
                tags = tags[0: len(tags) - 2]
                self.entity.setValue(tags=tags)


if __name__ == '__main__':
    from tools.myApp import MyApp

    app = MyApp()
    photoInfo = PhotoInformation2(app, "96452426")
    entity = photoInfo.work()
    print entity.getValue()
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
