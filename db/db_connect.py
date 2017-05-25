# __author__=xk
# -*- coding: utf-8 -*-
import MySQLdb
from tools.hostname import hostname
import logging
import logging.config
import os

def dbConnect():
    logFilepath = os.path.join(os.path.dirname(__file__), "../res/logging.conf")
    logging.config.fileConfig(logFilepath)
    logger = logging.getLogger("log")
    try:
        if hostname() == "DESKTOP-S1OH3KQ":
            host = "localhost"
        else:
            host = "223.3.93.40"
        logger.info("Trying to connect %s" % host)
        conn = MySQLdb.connect(host, 'dyn', '123', 'test')
        cur = conn.cursor()
        logger.info("Database Connected Successfully")
        return (conn, cur)
    except MySQLdb.Error as e:
        logger.error(e)
        return (None, None)


if __name__ == '__main__':
    conn, cur = dbConnect()
    cur.close()
    conn.close()


