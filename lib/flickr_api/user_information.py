# __author__=xk
# -*- coding: utf-8 -*-
import sys
from lib.flickr_api.abstract_api.flickr_user_api import FlickrUserApi

class UserInformation(FlickrUserApi):
    def __init__(self):
        super(UserInformation, self).__init__()
        self.api = "flickr.people.getInfo"

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
    from tools.my_app import MyApp
    app = MyApp()
    userInfo = UserInformation()
    userInfo.setApp(app)
    userInfo.setTaskId("100000122@N08")
    entity = userInfo.work()
    print entity.getValue()