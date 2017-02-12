# __author__=xk
# -*- coding: utf-8 -*-
class PhotoEntity:
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


if __name__ == '__main__':
    pass
