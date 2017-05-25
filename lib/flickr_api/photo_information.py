# __author__=xk
# -*- coding: utf-8 -*-
import sys
from tools.timestamp import timestampConvertToTime
from lib.flickr_api.abstract_api.flickr_photo_api import FlickrPhotoApi

class PhotoInformation(FlickrPhotoApi):
    def __init__(self):
        super(PhotoInformation, self).__init__()
        self.api = "flickr.photos.getInfo"

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
    from tools.my_app import MyApp
    app = MyApp()
    photoInfo = PhotoInformation()
    photoInfo.setApp(app)
    photoInfo.setTaskId("96452426")
    entity = photoInfo.work()
    print entity.getValue()