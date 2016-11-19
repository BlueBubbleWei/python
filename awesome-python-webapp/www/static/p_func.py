#!/usr/bin/python
# -*- coding:utf-8 -*-
def checkName(x,y):
    print x

    print y

name='Blue'
age=25

#virtual arguement
checkName('a',12)
#real arguement
checkName(name,age)

def strCmp(a,b):
    n=len(a)
    m=len(b)
    if n==m:
        i=0
        while i<n:
            if a[i] !=b[i] and i!=n-1:
                return ord(a[i])-ord(b[i])
    else:
        i=0
        while i<n:
            if a[i]!=b[i] and i!=n-1:
                return ord(a[i])-ord(b[i])
            if i!=n-1:
                if m>=n:
                    return 'b is bigger'
                else:
                    return 'a is bigger'
    i+=1

#the function is used to copy 

def strCpy(a,b):
    l=len(a)
    i=0
    while i<l:
        b+=a[i]
        i+=1
    return b

def strCat(a,b):
    l=len(b)
    i=0
    while i<l:
        a+=b[i]
        i=i+1
    return a

s='hello'
t='highftri'
r=strCmp(s,t)

a='copy'
b=''
r=strCpy(a,b)
#print r

a='hello'
b='world'
r=strCat(a,b)
print r



#print r
