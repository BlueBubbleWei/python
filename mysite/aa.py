#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
def main():
    from blog.models import Blog
    f=open('aa.txt')
    BlogList= []
    for line in f:
        title,content=line.splite('****')
        blog=Blog(title=title,content=content)
        BlogList.append(blog)
    f.close()

    Blog.objects.bulk_create(BlogList)

if __name__=="__main__":
    main()
    print('Done')




