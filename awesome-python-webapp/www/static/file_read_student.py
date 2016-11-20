#!/usr/bin/python
# -*- coding:utf-8 -*-

# splited the first linto word by word 
for info in open('student.txt','r').readline():
    print info

#print each line of the file
for info in open('student.txt','r').readlines():                          
    print info 
