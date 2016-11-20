#!/usr/bin/python
# -*- coding:utf-8 -*-


file=open('auto.txt','w')
a='hello'
b='Great'
file.write(a+'\n')
file.writelines([a,b,'\n'])

file.writelines((a,b,'\n'))
file.writelines({a,b,'\n'})
file.close()
