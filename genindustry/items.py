# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class GenindustryItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class NewsItem(scrapy.Item):
    title = scrapy.Field()#标题
    type = scrapy.Field()#类型
    content = scrapy.Field()#内容
    writer = scrapy.Field()#作者
    source = scrapy.Field()#来源
    sourcecategory = scrapy.Field()#资源类别
    pubdate = scrapy.Field()#发布日期
    create_date = scrapy.Field()#创建时间
    #recorddate = scrapy.Field#记录日期
    orgurl = scrapy.Field()#原始url
    tags = scrapy.Field()#标签
    opinion = scrapy.Field()#看法
    summary = scrapy.Field()#摘要
    remarks = scrapy.Field()#备注
    category_id = scrapy.Field()#栏目
    companyremark = scrapy.Field()#公司备注
    industryremark = scrapy.Field()#行业备注
    pararremark= scrapy.Field()#段落信息
    uuid = scrapy.Field()#uuid
