# __author__=xk
# -*- coding: utf-8 -*-

from abstract_DB_writing import AbstractDBWriting

class PhotoInformationWriting(AbstractDBWriting):
    def __init__(self):
        super(PhotoInformationWriting, self).__init__()

class PhotoUrlWriting(AbstractDBWriting):
    def __init__(self):
        super(PhotoUrlWriting, self).__init__()

class UserInformationWriting(AbstractDBWriting):
    def __init__(self):
        super(UserInformationWriting, self).__init__()

class UserFollowersWriting(AbstractDBWriting):
    def __init__(self):
        super(UserFollowersWriting, self).__init__()

class UserPhotosWriting(AbstractDBWriting):
    def __init__(self):
        super(UserPhotosWriting, self).__init__()


if __name__ == '__main__':
    pass