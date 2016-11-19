#!/usr/bin/python
# -*- coding:utf-8 -*-

mmurl="https://mm.taobao.com/json/request_top_list.htm?type=0&page="
i=0
while i<20:
    url=mmurl+str(i)
    i=i+1
    print url
