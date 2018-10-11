#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/9/30 17:38
# file:log
# desc:

import logging
from datetime import datetime
import threading
import os

class Log:
    def __init__(self):
        global logPath,reportPath
        reportPath = os.path.abspath(os.path.join(os.getcwd(),'../report'))
        if not os.path.exists(reportPath):
            os.mkdir(reportPath)
        logPath = os.path.join(reportPath,str(datetime.now().strftime('%Y%m%d%H%M%S')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(os.path.join(logPath,"output.log"))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

