# __author__=xk
# -*- coding: utf-8 -*-
from entity.abstract_entity.abstract_user_entity import AbstractUserEntity
from entity.abstract_entity.abstract_photo_entity import AbstractPhotoEntity


class PhotoInformationEntity(AbstractPhotoEntity):
    def __init__(self, photoid):
        super(PhotoInformationEntity, self).__init__(photoid)
        self.filedName = ["views", "title", "dates", "comments", "tags"]
        self.filedSize = 5
        self.setFiledInitValues(0, None, None, 0, None)


class PhotoUrlEntity(AbstractPhotoEntity):
    def __init__(self, photoid):
        super(PhotoUrlEntity, self).__init__(photoid)
        self.filedName = ["downloadurl"]
        self.filedSize = 1
        self.setFiledInitValues(None)


class UserInformationEntity(AbstractUserEntity):
    def __init__(self, uid):
        super(UserInformationEntity, self).__init__(uid)
        self.filedName = ["username", "realname", "location", "photosurl", "profileurl", "photocount", "firstdatetaken"]
        self.filedSize = 7
        self.setFiledInitValues(None, None, None, None, None, 0, None)


class UserFollowersEntity(AbstractUserEntity):
    def __init__(self, uid):
        super(UserFollowersEntity, self).__init__(uid)
        self.filedName = ["uid", "follower"]
        self.filedSize = 2
        self.setFiledInitValues(None, None)


class UserPhotosEntity(AbstractUserEntity):
    def __init__(self, uid):
        super(UserPhotosEntity, self).__init__(uid)
        self.filedName = ["photoid"]
        self.filedSize = 1
        self.setFiledInitValues(None, self.uid)


if __name__ == '__main__':
    pass