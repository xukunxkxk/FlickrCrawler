# __author__=xk
# -*- coding: utf-8 -*-
from time import localtime, strftime, mktime, strptime


def timestampConvertToTime(timestamp):
    return strftime('%Y-%m-%d %H:%M:%S', localtime(float(timestamp)))


def timeConvertToTimestamp(time):
    return int(mktime(strptime(time, "%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    print timestampConvertToTime("1474214427")
    print timeConvertToTimestamp("2016-09-19 00:00:27")