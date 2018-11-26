#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/12 18:01
# file:mylog
# desc: 日志工具类

import logging
import os
from util import glb

logPath = glb.reportPath

if not os.path.exists(logPath):
    os.mkdir(logPath)
logfile = os.path.join(logPath,'output.log')

class Log(object):
    ''' '''
    def __init__(self, name):
        self.logfile = logfile
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # 输出日志到文件
        handler = logging.FileHandler(self.logfile, encoding='utf-8')
        self.fh = handler
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        # 输出日志到控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)


    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def close(self):
        self.logger.removeHandler(self.fh)

if __name__ == '__main__':
    logger = Log('testlog')
    logger.info('suheping')
