#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/9/29 17:29
# file:readXlsUtil
# desc: 读取excel测试数据文件工具类

import xlrd,os

class readXlsUtil():
    def __init__(self,xlsPath, sheetName):
        self.data = xlrd.open_workbook(xlsPath)
        self.sheetList = self.data.sheet_names()
        self.table = self.data.sheet_by_name(sheetName)
        # 读取第一行数据作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self,case_type):
        if self.rowNum <=1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                # 判断是否是要读取的用例类型
                # 0：预置用例   1：正常用例
                if values[-1] == str(case_type):
                    for x in list(range(self.colNum)):
                        s[self.keys[x]] = values[x]
                    r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = '../data/case_process.xlsx'
    sheetName = 'Sheet2'
    data = readXlsUtil(filepath,sheetName)
    print(data.dict_data(0))
    for i in data.dict_data(1):
        print(i['caseId'])
