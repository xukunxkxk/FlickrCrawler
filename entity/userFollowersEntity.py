# __author__=xk
# -*- coding: utf-8 -*-
class UserFollowersEntity:
    def __init__(self,uid):
        self.uid=uid
        self.followers=list()
        self.followersSize=0
        self.iterSize=0
    def addFollowers(self,follower):
        self.followers.append(follower)
        self.followersSize+=1

    def getUid(self):
        return self.uid
    def getFollowersSize(self):
        return self.followersSize



    #迭代器定义
    def next(self):
        if self.iterSize==self.followersSize:
            self.iterSize=0
            raise StopIteration
        self.iterSize+=1
        return self.followers[self.iterSize-1]
    def __iter__(self):
        return self


if __name__ == '__main__':
    a=UserFollowersEntity("11111")
    for i in range(10):
        a.addFollowers(str(i))
    for i in a:
        print i


