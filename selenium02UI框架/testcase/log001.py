# coding=utf-8
import logging
def logprint():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/tmp/testlog.log',
                        filemode='w')
    return logging
print logprint()
