#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
from img_spider.items import ImgSpiderItem
import urllib
import os
import time


def download_pic(url):
	first_name=url[-10]
	path='D:\\Apic\\'
	name=path+first_name.replace('/','_')
	if not os.path.exists(name):
		data=urllib.urlretrieve(url,name)
		print 'downloading now.'
		time.sleep(2)
	else:
		print 'this pic exsits error'
def DeseSpider(scrapy.Spider):
	name='desk'
	allowed_domains=['desk.zol.com.cn']
	start_url=['http://desk.zol.com.cn/1920x1080/',]
	
	def parse(self,response):
	for href in response.xpath('//ul[@class="pic-list2 clearfix"]/li/a/@href').extract()
		yield scrapy.Request('http://desk.zol.com.cn'+href,callback=self.parse_url)
	page_link=response.xpath('//div[@class="page"]/a/@href').extract()
	full_page_link='http://desk.zol.com.cn'+page_link[-1]
	yield scrapy.Request(full_page_link,callback=self.parse)


def parse_url(self,response):
	item=ImgSpiderItem()
	img=response.xpath('//ul[@id="showImg"]/li/a/img').extract()
	reg=(r'http.=\.jpg')
	for i in imgs:
		img=re.findall(reg,i)
		item['img']=img
		for url in item['img']:
			download_pic(url)
			print '-'*100
