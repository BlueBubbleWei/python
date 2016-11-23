#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Article,Person
# Register your models here.

#admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','pub_date','upd_date',)
    def save_model(self,request,obj,form,change):
        if change:
            obj_original=self.model.objects.get(pk=obj.pk)
        else:
            obj_original=None
        obj.user=request.user
        obj.save()

    def delete_model(self,request,obj):
        obj.delete()

class PersonAdmin(admin.ModelAdmin):
    list_display=('name','age')
    search_fields=('name',)
    def get_search_results(self,request,queryset,search_term):
        queryset,use_distict=super(PersonAdmin,self).get_search_results(request,queryset,search_term)
        try:
            search_term_as_int=int(search_term)
            queryset |=self.model.objects.filter(age=search_term_as_int)
        except:
            return search_term_as_int
        return queryset,use_distinct

#该类实现的功能是如果是超级管理员就列出所有的
#如果不是，就仅列出访问者自己相关的
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        qs=super(MyModelAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
