# __author__=xk
# -*- coding: utf-8 -*-
from entity import Entity


class AbstractPhotoEntity(Entity):
    def __init__(self, photoid):
        super(AbstractPhotoEntity, self).__init__()
        self.uid = photoid


if __name__ == '__main__':
    pass