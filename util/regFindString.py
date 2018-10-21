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

    tmp = {}

    s1 = "var tableKey = '201810207131C9157F2D4FE3A59C111'; // 桌台码  " \
         "var orderKey = '7131C9157F2D4FE3A59C_o29U5wq7XF-OutcJRojtmO2exjhY_orders';"

    js = "{\"tablekey\":\"tableKey = '(.+?)';\",\"orderKey\":\"orderKey = '(.+?)';\"}"

    params = regFindString(s1,js).find()
    print(params)
    for i in params:
        tmp[i] = params[i]
        print(tmp)

    s2 = "var tableKey = '201810207131C9157F2D4FE3A59C111'; // 桌台码  " \
         "var orderid = '7131C9157F2D4FE3A59C_o29U5wq7XF-OutcJRojtmO2exjhY_orders';"

    js2 = "{\"tablekey\":\"tableKey = '(.+?)';\",\"orderid\":\"orderid = '(.+?)';\"}"

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


