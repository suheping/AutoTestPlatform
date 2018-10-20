#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/20 18:33
# file:regFindString
# desc: 通过正则取值,传入多个正则的键值对，返回多个键值对

import re,json

class regFindString:
    def __init__(self,str,regs):
        self.str = str
        self.regs = regs


    def find(self):
        reg = json.loads(self.regs)
        res = {}
        for i in reg.keys():
            r = re.findall(reg[i], self.str)
            if r:
                res[i] = r[0]
            else:
                res[i] = ''
        return res


if __name__ == "__main__":

    s1 = "var tableKey = '201810207131C9157F2D4FE3A59C111'; // 桌台码  " \
         "var orderKey = '7131C9157F2D4FE3A59C_o29U5wq7XF-OutcJRojtmO2exjhY_orders';"

    js = "{\"tablekey\":\"tableKey = '(.+?)';\",\"orderKey\":\"orderKey = '(.+?)';\"}"

    params = regFindString(s1,js).find()

    body = '{"tableKey":"${tablekey}","soupOrder":"Y","orderKey":"${orderKey}"}'


    l = re.findall("\${(.+?)}",body)
    print(l)
    for i in l:
        body = body.replace("${"+ i +"}",params[i])
    print(body)


