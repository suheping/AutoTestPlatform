#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/20 18:33
# file:regFindString
# desc: 通过正则取值,传入多个正则的键值对，返回多个键值对

import re,json
import json.decoder
from util.logUtil import Log

logger = Log('regFindString')

class regFindString:
    def __init__(self,str,regs):
        self.str = str
        self.regs = regs


    def find(self):
        res = {}
        ''' 20190522修改，捕获string转字典异常，并打印错误日志'''
        try:
            # string转为字典格式
            reg = json.loads(self.regs)
            for i in reg.keys():
                r = re.findall(reg[i], self.str)
                if r:
                    res[i] = r[0]
                else:
                    res[i] = ''
        except json.decoder.JSONDecodeError as e:
            # print("re字段不是标准json，请确认！,报错信息如下：",e)
            logger.error("re字段不是标准json，请确认！,报错信息如下：\n %s" % e)
        finally:
            return res


if __name__ == "__main__":

    tmp = {}

    s1 = '{"accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiIl0sInVzZXJfbmFtZSI6IntcIm1vYmlsZVwiOlwiMTgwMDU0MTAzNTBcIixcImFpZFwiOlwiNDdlMzYyNjZlNWFhNDc3ZThkYjlmZGM2ZjEyMTdjZDBcIixcInVpZFwiOlwiLTFcIixcInRpZFwiOlwiNWFiZjAwMTc5NmQxOTAwMDBkMDdhNTlhXCIsXCJzaWRcIjpcIjVlODJiYTNjLWM5ODItNDUxOS04NzFkLWIxZmNhN2I3YzFhMlwiLFwiYXRva2VuXCI6XCI0OWJhOWM2NjkyNzU0ZWZlYWJlZThlN2M3M2EzNmFkMVwifSIsInNjb3BlIjpbInNjb3BlIl0sImV4cCI6MTU1ODQ0NDk4NCwiYXV0aG9yaXRpZXMiOlsiVVNFUiJdLCJqdGkiOiI0OTJhYzIyNi00OWFmLTQyYzAtYTQyNi1kNjE2OGQyYTdhNWMiLCJjbGllbnRfaWQiOiJCcm93c2VyIn0.U07Cc9IkaSga-4si-nIrbo7mOCx2f_oNv4_Sdw8FGT1spxle6NmKHjZtT2a4ZI8IfHvL3qYxq9L7_7HCJbsHQVOMlSbHVkUzI__KYUgB72lANxGffRedq0CG5LXC1Ua5ArNXCBWJ6cfgXn1f5JH-WpGDmStBg_6MSRlmpToT6go","refreshToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiIl0sInVzZXJfbmFtZSI6IntcIm1vYmlsZVwiOlwiMTgwMDU0MTAzNTBcIixcImFpZFwiOlwiNDdlMzYyNjZlNWFhNDc3ZThkYjlmZGM2ZjEyMTdjZDBcIixcInVpZFwiOlwiLTFcIixcInRpZFwiOlwiNWFiZjAwMTc5NmQxOTAwMDBkMDdhNTlhXCIsXCJzaWRcIjpcIjVlODJiYTNjLWM5ODItNDUxOS04NzFkLWIxZmNhN2I3YzFhMlwiLFwiYXRva2VuXCI6XCI0OWJhOWM2NjkyNzU0ZWZlYWJlZThlN2M3M2EzNmFkMVwifSIsInNjb3BlIjpbInNjb3BlIl0sImF0aSI6IjQ5MmFjMjI2LTQ5YWYtNDJjMC1hNDI2LWQ2MTY4ZDJhN2E1YyIsImV4cCI6MTU1ODQ1MDM4NCwiYXV0aG9yaXRpZXMiOlsiVVNFUiJdLCJqdGkiOiJkMjIwM2YwZC1kYWRkLTQ4NTItYWFjNC00N2U2ODVkNDZlMDYiLCJjbGllbnRfaWQiOiJCcm93c2VyIn0.Wm3aSeovA32vtiCxAZm98z0XgiWbjQV7NTEMymw07MZ3XxhJ3xZJ7QHl_aTfaqTEiXteQnZUzrVwkW8WTQbRUoBsPVk3YaCFP6FPt0HO0vD9rdT5da-mX2q-QQv2-0_Lqegl8S2AwK2ka7bV7C8SxxX-UF24e7xv1hZEOHJRUVQ._f344b80e4120446d9835d8725ac9b8b3_."}'
    dic_a = json.loads(s1)
    print(dic_a["accessToken"])
    # js = "{\"accessToken\": \"a\"}"
    # js = "{'accessToken': 'accessToken\": \"(.+?)\"'}"
    # js = "{"accessToken": "accessToken\": \"(.+?)\","}"
    js = '{"accessToken": "accessToken\\\": \\\"(.+?)\\\",","refreshToken": "refreshToken\\\": \\\"(.+?)\\\""}'
    # dic_b = json.loads(js1)
    # print(dic_b["accessToken"])

    params = regFindString(s1,js).find()
    print(params)
    for i in params:
        tmp[i] = params[i]
        print(tmp)

    s2 = "var tableKey = '201810207131C9157F2D4FE3A59C111'; // 桌台码  " \
         "var orderid = '7131C9157F2D4FE3A59C_o29U5wq7XF-OutcJRojtmO2exjhY_orders';"

    js2 = "{\"tablekey\":\"tableKey = '(.+?)';\",\"orderid\":\"orderid = '(.+?)';\"}"

    # js3 = "{"tablekey":"tableKey = '(.+?)';","orderid":"orderid = '(.+?)';"}"

    params2 = regFindString(s2,js2).find()

    print(params2)
    for j in params2:
        tmp[j] = params2[j]

    print(tmp)




    # body = '{"tableKey":"${tablekey}","soupOrder":"Y","orderKey":"${orderKey}"}'
    #
    #
    # l = re.findall("\${(.+?)}",body)
    # print(l)
    # for i in l:
    #     body = body.replace("${"+ i +"}",params[i])
    # print(body)


