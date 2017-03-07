# __author__=xk
# -*- coding: utf-8 -*-



if __name__ == '__main__':
    import logging
    import logging.config

    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s' ,
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename='myapp.log',
    #                     filemode='w')
    # console = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    # console.setFormatter(formatter)
    # logging.getLogger('').addHandler(console)
    # logging.debug('This is debug message')
    # logging.info('This is info message')
    # logging.warning('This is warning message')


    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("example01")

    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')