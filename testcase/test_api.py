#-*- coding:utf-8 -*-


import unittest
import ddt
import os
import requests
from util.baseApi import sendRequest,writeResult2,writeResult
from util.copyXls import copyXls
from util.readXlsUtil import readXlsUtil
from util.loadConf import loadConf
from util import glb

# 获取data、report目录
dataPath = glb.dataPath
reportPath = glb.reportPath

datafile = loadConf.get_config('test_api','data_file')
reportfile = loadConf.get_config('test_api','report_file')

dataXls = os.path.join(dataPath,datafile)
reportXls = os.path.join(reportPath,reportfile)

# 读取测试用例
testData_pre = readXlsUtil(dataXls,'Sheet1').dict_data(0)
testData_norm = readXlsUtil(dataXls,'Sheet1').dict_data(1)

print("testData_norm:%s\n"%testData_norm)


@ddt.ddt
class MyTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        copyXls(dataXls,reportXls)
        print('testData_pre:%s'%testData_pre)
        for i in testData_pre:
            print('testData_pre里的元素：%s'%i)
            result = sendRequest(cls.session,i)
            writeResult(result,reportXls)

    @ddt.data(*testData_norm)
    def test_something(self,data):
        print('data:%s\n'%data)
        result = sendRequest(self.session,data)
        writeResult(result,reportXls)
        check = data['checkpoint']
        # print('检查点是：%s' % check)
        resText = result['text']
        # print("实际返回结果为：%s" % resText)

        self.assertIn(check,resText)

if __name__ == '__main__':
    unittest.main()