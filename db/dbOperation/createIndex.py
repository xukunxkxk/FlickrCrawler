# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from db.dbConnect import dbConnect


def createIndex():
    conn, cur = dbConnect()
    for i in range(2, 3):
        try:
            tableName = "photos_" + str(i)
            sql = "CREATE UNIQUE INDEX photoidOwner ON " + tableName + "(photoid,owner)"
            cur.execute(sql)
        except MySQLdb.Error as e:
            print e

'''
 delete from photos_2 where photoid
 in (select photoid from photos_2 group by photoid having count(*)>1)
 and id not in (select min(id) from photos_2 group by photoid having count(*)>1);

insert into photos_1(a,b) select a,b from photos_0 where owner like '%1'
'''


if __name__ == '__main__':
    createIndex()
