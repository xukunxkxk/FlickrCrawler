# __author__=xk
# -*- coding: utf-8 -*-
from baseEntity.abstractUserEntity import AbstractUserEntity
class UserEntity:
    def __init__(self, uid):
        self.uid = uid
        self.username = None
        self.realname = None
        self.location = None
        self.photosurl = None
        self.profileurl = None
        self.photocount = 0
        self.firstdatetaken = None

    def getUid(self):
        return self.uid

    def setValue(self, userInformation):
        self.username = userInformation[0]
        self.realname = userInformation[1]
        self.location = userInformation[2]
        self.photosurl = userInformation[3]
        self.profileurl = userInformation[4]
        self.photocount = userInformation[5]
        self.firstdatetaken = userInformation[6]

    def setUsername(self, username):
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


class UserEntity2(AbstractUserEntity):
    def __init__(self, uid):
        super(UserEntity2, self).__init__(uid)
        self.filedName = ["username", "realname", "location", "photosurl", "profileurl", "photocount", "firstdatetaken"]
        self.filedSize = 7
        self.setFiledInitValues(None, None, None, None, None, 0, None)

if __name__ == '__main__':
    u = UserEntity2("1111")
    print u.getValue()
    dic = {'username': 2, 'photocount': 3, 'realname': 2, 'profileurl': 5, 'firstdatetaken': 6, 'photosurl': 4, 'location': 3}
    u.setValue(photocount = 3)
    u.setValue(a = 2)
    print u.getValue()


