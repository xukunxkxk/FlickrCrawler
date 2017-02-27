# __author__=xk
# -*- coding: utf-8 -*-
from baseEntity.abstractPhotoEntity import AbstractPhotoEntity
class PhotoEntity():
    def __init__(self, photoId):
        self.photoId = photoId
        self.views = 0
        self.title = None
        self.dates = None
        self.comments = 0
        self.tags = None

    def getPhotoId(self):
        return self.photoId

    def getValue(self):
        return (self.views, self.title, self.dates, self.comments, self.tags, self.photoId)

    def setValue(self, views, title, dates, comments, tags):
        self.views = views
        self.title = title
        self.dates = dates
        self.comments = comments
        self.tags = tags

class PhotoEntity2(AbstractPhotoEntity):
    def __init__(self, photoid):
        super(PhotoEntity2, self).__init__(photoid)
        self.filedName = ["views", "title", "dates", "comments", "tags"]
        self.filedSize = 5
        self.setFiledInitValues(0, None, None, 0, None)




if __name__ == '__main__':
    p = PhotoEntity2("1111")
    print p.getValue()
    print p.getId()
    p.setValue(views = 2)
    p.setValue(title = "11")
    p.setValue(dates = "22222")
    p.setValue(comments = 2)
    p.setValue(tags = "222")
    print p.getValue()
