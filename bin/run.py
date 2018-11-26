#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/9/30 16:52
# file:run
# desc: 入口

import unittest
import os,time
from util import HTMLTestRunner_api
from util import glb
from util.loadConf import loadConf


reportPath = glb.reportPath
casePath = os.path.abspath(os.path.join(os.getcwd(),'../testcase'))


def add_case(casePath,rule):
    discover = unittest.defaultTestLoader.discover(casePath,pattern=rule)
    return discover

def run_case(allCase):
    ctime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # 定义报告文件名称
    htmlReport= reportPath + r'\report_'+ ctime + '.html'
    fp = open(htmlReport,'wb')
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title='自动化测试报告',
                                               description='用例执行情况')
    runner.run(allCase)
    fp.close()
    return htmlReport

if __name__ == '__main__':
    # 收集需要测试的用例
    rule = loadConf.get_config('run','rule')
    cases = add_case(casePath,rule)
    # 执行用例
    reportfile = run_case(cases)
    # 发送邮件
    content = open(reportfile,'rb')




