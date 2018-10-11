#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/8 10:00
# file:test_smdc
# desc: 测试呷哺扫码点餐，备注：需要先扫码保持session


import unittest
import os,time
import requests
import ddt
from util.baseApi import sendRequest,writeResult
from util.copyXls import copyXls
from util.readXlsUtil import readXlsUtil



# 当获取data目录
dataPath = os.path.abspath(os.path.join(os.getcwd(), "../data"))
reportPath = os.path.abspath(os.path.join(os.getcwd(),'../report'))

dataXls = os.path.join(dataPath,'case_smdc.xlsx')
reportXls = os.path.join(reportPath,'case_smdc_result.xlsx')

# 读取测试数据
testData_pre = readXlsUtil(dataXls).dict_data(0)
testData_norm = readXlsUtil(dataXls).dict_data(1)


@ddt.ddt
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        copyXls(dataXls, reportXls)
        cls.session = requests.session()
        for i in testData_pre:
            print(i)
            result = sendRequest(cls.session,i)
            writeResult(result,reportXls)


    @ddt.data(*testData_norm)
    def test_something(self,data):
        time.sleep(2)
        result = sendRequest(self.session, data)
        writeResult(result, reportXls)
        check = data['checkpoint']
        # print('检查点是：%s' % check)
        resText = result['text']
        # print("实际返回结果为：%s" % resText)
        self.assertIn(check,resText)


if __name__ == '__main__':
    unittest.main()
