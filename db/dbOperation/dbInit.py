# __author__=xk
# -*- coding: utf-8 -*-
from db.dbOperation.dbCreate import dbCreate
from  tableCreate import tableCreate


def dbInit():
    dbCreate()
    tableCreate()


if __name__ == '__main__':
    dbInit()
