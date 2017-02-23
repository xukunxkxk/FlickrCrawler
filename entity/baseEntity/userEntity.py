# __author__=xk
# -*- coding: utf-8 -*-
from entity import Entity

class AbstractUserEntity(Entity):
    def __init__(self, uid):
        super(AbstractUserEntity, self).__init__()
        self.uid = uid

if __name__ == '__main__':
    pass