#-*- coding:utf-8 -*-


import unittest
import ddt
import os
import requests
from util.baseApi import sendRequest,writeResult
from util.copyXls import copyXls
from util.readXlsUtil import readXlsUtil
from util.loadConf import loadConf
from util import glb
from util.logUtil import Log
from util.replace import replace
from util.regFindString import regFindString

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

logger = Log("test_api")

@ddt.ddt
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        copyXls(dataXls,reportXls)

        # 保存所有从响应中取出来的参数及值
        cls.tmp = {}
        # 开始前置用例的测试
        for i in testData_pre:
            if cls.tmp == {}:
                logger.info("用例%s 没有关联参数" % i['caseId'])
            else:
                # 如果有关联参数，替换body、params、url
                i['body'] = replace(i['body'], cls.tmp).replace()
                i['params'] = replace(i['params'], cls.tmp).replace()
                i['url'] = replace(i['url'], cls.tmp).replace()
            # 发送请求
            result = sendRequest(cls.session,i)
            # 如果存在re，就去响应中查找，找到后存到tmp中
            if i['re']:
                param = regFindString(result['text'],i['re']).find()
                for j in param:
                    cls.tmp[j] = param[j]
            # 写结果
            writeResult(result,reportXls)

    @ddt.data(*testData_norm)
    def test_something(self,data):

        # 判断是否有取到的参数
        if self.tmp == {}:
            logger.info("用例%s 没有关联参数" % data['caseId'])
        else:
            # 如果有关联参数，替换body、params、url
            data['body'] = replace(data['body'], self.tmp).replace()
            data['params'] = replace(data['params'], self.tmp).replace()
            data['url'] = replace(data['url'], self.tmp).replace()
        # 发送请求
        result = sendRequest(self.session,data)
        # 如果存在re，就去响应中查找，找到后存到tmp中
        if data['re']:
            param = regFindString(result['text'], data['re']).find()
            for j in param:
                self.tmp[j] = param[j]
        # 写结果
        writeResult(result,reportXls)
        # 开始断言
        check = data['checkpoint']
        resText = result['text']
        self.assertIn(check,resText)

if __name__ == '__main__':
    unittest.main()