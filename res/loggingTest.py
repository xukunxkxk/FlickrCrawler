# __author__=xk
# -*- coding: utf-8 -*-



if __name__ == '__main__':
    import logging
    import logging.config
    import os
    logfilepath = os.path.join(os.path.dirname('__file_'), "../res/logging.conf")
    logging.config.fileConfig(logfilepath)
    logger = logging.getLogger("apilogHandler")

    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')