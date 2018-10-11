#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/9/30 16:52
# file:run
# desc: 入口

import unittest
import os
import time
from util import HTMLTestRunner_api

reportPath = os.path.abspath(os.path.join(os.getcwd(),'../report'))
if not os.path.exists(reportPath):
    os.mkdir(reportPath)
casePath = os.path.abspath(os.path.join(os.getcwd(),'../testcase'))

def add_case(casePath=casePath,rule="test_smdc.py"):
    discover = unittest.defaultTestLoader.discover(casePath,pattern=rule)
    return discover

def run_case(allCase):
    htmlReport = reportPath + r'\result.html'
    print("测试报告是：%s" % htmlReport)
    fp = open(htmlReport,'wb')
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title='自动化测试报告',
                                               description='用例执行情况')
    runner.run(allCase)
    fp.close()

if __name__ == '__main__':
    cases = add_case()
    run_case(cases)