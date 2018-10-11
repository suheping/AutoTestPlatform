#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/9/30 10:48
# file:baseApi
# desc: 封装http请求，写测试结果

import json
import requests
from util.copyXls import writeXls,copyXls
from util.readXlsUtil import readXlsUtil
from util.log import MyLog

logger = MyLog.get_log()
def sendRequest(session,testData):
    '''封装requests请求'''
    caseId = testData['caseId']
    method = testData['method']
    url = testData['url']
    try:
        params = eval(testData['params'])
    except:
        params = None

    try:
        headers = eval(testData['headers'])
    except:
        headers = None
    bodyType = testData['bodyType']

    print("*******正在执行用例：-----  %s  ----**********" % caseId)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    try:
        body = eval(testData['body'])
    except:
        body = {}

    if bodyType == 'json':
        body = json.dumps(body)
    else:
        body = body
    if method == 'post':
        print("post请求body类型为：%s，body内容为：%s" % (bodyType,body))

    verify = False
    result = {}

    try:
        response = session.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                       )

        print('请求的cookie为：%s' % session.cookies)
        print('返回的cookie为：%s' %response.cookies)
        print("返回信息：%s" % response.content.decode('utf-8'))
        result['id'] = testData['caseId']
        result['rowNum'] = testData['rowNum']
        result["statusCode"] = str(response.status_code)  # 状态码转成str
        result["text"] = response.content.decode("utf-8")
        result["times"] = str(response.elapsed.total_seconds())  # 接口请求时间转str
        if result["statusCode"] != "200":
            result["error"] = result["text"]
        else:
            result["error"] = ""

        type(result['text'])

        if testData["checkpoint"] in result["text"]:
            result["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (caseId, result["result"]))
        else:
            result["result"] = "fail"

        return result
    except Exception as e :
        result['error'] = str(e)
        result['result'] = 'fail'
        return result

def writeResult(result,filename):
    rowNum = result['rowNum']
    wt = writeXls(filename)
    wt.write(rowNum,9,result['statusCode'])
    wt.write(rowNum,10,result['text'])
    wt.write(rowNum,11,result['error'])
    wt.write(rowNum,12,result['times'])
    wt.write(rowNum,13,result['result'])


if __name__ == '__main__':
    testData = readXlsUtil('../data/case1.xlsx').dict_data()
    print(testData[0])
    session = requests.session()
    result = sendRequest(session,testData[0])
    copyXls('../data/case1.xlsx','../report/case1_result.xlsx')
    writeResult(result,'../report/case1_result.xlsx')
