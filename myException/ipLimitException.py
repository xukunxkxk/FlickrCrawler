# __author__=xk
# -*- coding: utf-8 -*-
class IpLimitException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    pass