#coding:utf-8
import os,sys
#我是注释
'''
option = sys.argv[1]
if option=='version':
    print 'version 1.0'
'''
lists = ['a','b','\n','\n',r'\n']
for each in lists:
    if each == r'\n':
        print 'empty'
