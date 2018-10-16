#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/16 14:40
# file:readXlsUtil2
# desc: 读取测试数据


import xlrd,os
from util.readXlsUtil import readXlsUtil

class readXlsUtil2():
    def __init__(self,xlsPath):
        self.xlsPath = xlsPath
        self.data = xlrd.open_workbook(xlsPath)
        self.sheetList = self.data.sheet_names()
        print(self.sheetList)
        # self.table = self.data.sheet_by_name(sheetName)
        # # 读取第一行数据作为key值
        # self.keys = self.table.row_values(0)
        # # 获取总行数
        # self.rowNum = self.table.nrows
        # # 获取总列数
        # self.colNum = self.table.ncols

    def dict_data(self,case_type):
        dict_data = []
        r =[]
        for sheet in self.sheetList:
            # 取到当前sheet的值
            table = self.data.sheet_by_name(sheet)
            # 取到第一行的key
            keys = table.row_values(0)
            # 取到总行数、总列数
            rowCount = table.nrows
            print(rowCount)
            colCount = table.ncols
            print(colCount)

            if rowCount <=1:   # 如果总行数小于等于1，也就是没有数据
                print("未在%s的%s中找到测试数据"%(self.xlsPath,sheet))
            else:  # 如果总行数>1
                # r = []
                j = 1
                for i in list(range(rowCount - 1)):
                    s = {}
                    s['sheetName'] = sheet
                    # 从第二行取对应values值
                    s['rowNum'] = i + 2
                    values = table.row_values(j)
                    # 判断是否是要读取的用例类型
                    # 0：预置用例   1：正常用例
                    if values[-1] == str(case_type):
                        for x in list(range(colCount)):
                            s[keys[x]] = values[x]
                        r.append(s)
                    j += 1
                # dict_data.append(r)
        # return dict_data
        return r

if __name__ == "__main__":
    filepath = '../data/case_process.xlsx'
    # sheetName = 'Sheet2'
    data = readXlsUtil2(filepath)
    # print(len(data.dict_data(1)))
    print(data.dict_data(1))
    print('\n')
    print(readXlsUtil(filepath,'Sheet1').dict_data(1))
    # print(data.dict_data(1))
    # for i in data.dict_data(1):
    #     print(i['caseId'])