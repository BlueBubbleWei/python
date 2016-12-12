from django.contrib import admin

# Register your models here.
from .models import Column,Article
class ColumnAdmin(admin.ModelAdmin):
	"""docstring for ColumnAdmin"""
	list_display=('name','slug','intro','nav_display','home_display')

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','pub_date','update_time')


admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
