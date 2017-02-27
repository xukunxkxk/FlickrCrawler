# __author__=xk
# -*- coding: utf-8 -*-
from baseEntity.abstractUserEntity import AbstractUserEntity
class UserFollowersEntity:
    def __init__(self, uid):
        self.uid = uid
        self.followers = list()
        self.followersSize = 0
        self.iterSize = 0

    def addFollowers(self, follower):
        self.followers.append(follower)
        self.followersSize += 1

    def getUid(self):
        return self.uid

    def getFollowersSize(self):
        return self.followersSize

    # 迭代器定义
    def next(self):
        if self.iterSize == self.followersSize:
            self.iterSize = 0
            raise StopIteration
        self.iterSize += 1
        return self.followers[self.iterSize - 1]

    def __iter__(self):
        return self


class UserFollowersEntity2(AbstractUserEntity):
    def __init__(self, uid):
        super(UserFollowersEntity2, self).__init__(uid)
        self.filedName = ["uid", "follower"]
        self.filedSize = 2
        self.setFiledInitValues(None, None)

if __name__ == '__main__':
    a = UserFollowersEntity2("11111")
    print a.getValue()
    print a.getId()
    a.setValue(uid = 2)
    a.setValue(follower = 3)
    print a.getValue()

