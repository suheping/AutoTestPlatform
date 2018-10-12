#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/12 21:49
# file:glb.py
# desc: 定义全局变量
import os,time

reportPath_base = os.path.abspath(os.path.join(os.getcwd(),'../report'))
if not os.path.exists(reportPath_base):
    os.mkdir(reportPath_base)
ctime: str = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
reportPath = os.path.join(reportPath_base,ctime)

dataPath = os.path.abspath(os.path.join(os.getcwd(),'../data'))