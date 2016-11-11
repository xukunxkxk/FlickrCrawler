# __author__=xk
# -*- coding: utf-8 -*-
class UserEntity:
    def __init__(self,uid):
        self.uid=uid
        self.username=None
        self.realname=None
        self.location=None
        self.photosurl = None
        self.profileurl=None
        self.photocount=0
        self.firstdatetaken=None

    def getUid(self):
        return self.uid

    def getValue(self):
        return (self.username,self.realname,self.location,self.photosurl,self.profileurl,self.photocount,self.firstdatetaken,self.uid)

    def setValue(self,userInformation):
        self.username=userInformation[0]
        self.realname=userInformation[1]
        self.location=userInformation[2]
        self.photosurl = userInformation[3]
        self.profileurl=userInformation[4]
        self.photocount=userInformation[5]
        self.firstdatetaken=userInformation[6]

    def setUsername(self,username):
        self.username = username
    def setRealname(self, realname):
        self.realname = realname
    def setLocation(self, location):
        self.location = location
    def setPhotosurl(self, photosurl):
        self.photosurl = photosurl
    def setProfileurl(self, profileurl):
        self.profileurl = profileurl
    def setPhotocount(self, photocount):
        self.photocount = photocount
    def setFirstdatetaken(self, firstdatetaken):
        self.firstdatetaken = firstdatetaken


if __name__ == '__main__':
    pass
    #https://api.flickr.com/services/rest/?&method=flickr.people.getInfo&api_key=d5a563f93922b2042cfe683bd1f16f38d&user_id=95200220@N03