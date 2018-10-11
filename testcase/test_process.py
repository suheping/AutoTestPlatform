#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/8 17:19
# file:test_process
# desc: 流程测试用例


import unittest
import requests
import os
from util.baseApi import sendRequest,writeResult
from util.copyXls import copyXls
from util.readXlsUtil import readXlsUtil


# 当获取data目录
dataPath = os.path.abspath(os.path.join(os.getcwd(), "../data"))
reportPath = os.path.abspath(os.path.join(os.getcwd(),'../report'))

dataXls = os.path.join(dataPath,'case_process.xlsx')
reportXls = os.path.join(reportPath,'case_process_result.xlsx')

# 读取测试数据
testData_pre = readXlsUtil(dataXls).dict_data(0)
testData_norm = readXlsUtil(dataXls).dict_data(1)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        copyXls(dataXls, reportXls)
        for i in testData_pre:
            result = sendRequest(cls.session,i)
            writeResult(result,reportXls)


    def test_something(self):

        for i in testData_norm:
            result = sendRequest(self.session,i)
            writeResult(result,reportXls)

        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
