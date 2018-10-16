#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/8 17:19
# file:test_process
# desc: 流程测试用例


import unittest
import requests
import os
from util.baseApi import sendRequest,writeResult,writeResult2
from util.copyXls import copyXls
from util.readXlsUtil2 import readXlsUtil2
from util.loadConf import loadConf
from util import glb

# 当获取data目录
dataPath = glb.dataPath
reportPath = glb.reportPath

dataXls = os.path.join(dataPath,loadConf.get_config('test_process','data_file'))
reportXls = os.path.join(reportPath,loadConf.get_config('test_process','report_file'))

# 读取测试数据
testData_pre = readXlsUtil2(dataXls).dict_data(0)
testData_norm = readXlsUtil2(dataXls).dict_data(1)
print('testData_norm:%s\n'%testData_norm)

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        copyXls(dataXls, reportXls)
        # for i in testData_pre:
        #     result = sendRequest(cls.session,i)
        #     writeResult(result,reportXls)


    def test_something(self):
        for data in testData_norm:
            print('data:%s\n'%data)
            # for i in data:
            result = sendRequest(self.session,data)
            # writeResult(result,reportXls)
            writeResult2(result,reportXls)
        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
