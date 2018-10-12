#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : genspiders.py
@创建时间：2018/10/12 12:05
'''
import scrapy
from bs4 import BeautifulSoup
from genindustry.items import NewsItem
from genindustry.dateutils import DateUtils
from tools.utils import Utils
from genindustry.geturlbyname import GetUrlByName
import datetime
import re
import sys
import json
import time
from genindustry.parseutils import ParseUtils
import uuid
reload(sys)
sys.setdefaultencoding('utf-8')

now_date = DateUtils()
parse_utils = ParseUtils()
get_url_by_name = GetUrlByName()
utils = Utils()

class slzcSpiders(scrapy.Spider):
    def __init__(self):
        self.static_url = 'http://www.slrbs.com'
    name = 'test'
    def start_requests(self):
        pages = []
        for i in range(1, 2):#1,592
            if i == 1:
                 url = 'http://www.slrbs.com/news/index.html'
            else:
                 url = 'http://www.slrbs.com/news/index_'+str(i)+'.html'
            page = scrapy.Request(url)
            pages.append(page)
        return pages
        #print ('pages', pages)


    def parse(self, response):
        dl_lists = response.xpath('//div[@class="ej_list_box clear"]/ul[@class="list_16 mt10"]')
        #遍历每个ul
        for dl_list in dl_lists:
            #遍历每个ul下面的li
            for li_li in dl_list.xpath('./li'):
                item = NewsItem()
                title = li_li.xpath('./a/text()').extract_first()
                orgurl_str = li_li.xpath('./a/@href').extract_first()
                orgurl_str = self.static_url+orgurl_str
                orgurl = orgurl_str
                #summary = dl_list.xpath('./p[@class="ltid"]/text()').extract_first()
                pubdate_str = dl_list.xpath('./p[@class="ltid"]/span[@class="ltit_d"]/text()').extract_first()
                #pubdate_str = utils.replace_str_null(pubdate_str, '发布：')
                #pubdate = utils.date_replace_lines(pubdate_str)
                srouce_category = None
                item['title'] = title
                #item['source'] = source_str
                item['orgurl'] = orgurl
                #item['pubdate'] = pubdate_str
                item['summary'] = None
                #item['sourcecategory'] = srouce_category

                if orgurl is not None:
                    request = scrapy.Request(orgurl, callback=self.parse_item)
                    request.meta['item'] = item
                    yield request


    def parse_item(self, response):
        item = response.meta['item']
        data = response.xpath("//div[@id='article_content']") #获取<p>标签下的所有内容
        if len(data)<=0:
             data = response.xpath("//div[@class='highlight']") #获取<p>标签下的所有内容
        content_str = data.xpath('string(.)').extract_first() #用正则表达式匹配字符串
        content = utils.str_strip_remove_tnr(content_str)
        pubdate_str = response.xpath('//div[@class="headtitle"]/span/text()').extract_first()
        pubdate = utils.remove_tnr(pubdate_str)
        source_str = ''
        source_str = response.xpath('//div[@class="headtitle"]/a/text()').extract_first()
        if source_str is not None:
            source_str=source_str
        else:
            source_str = response.xpath('//div[@class="headtitle"]/text()').extract_first()
        if content is not None:
            item['content'] = content
            item['sourcecategory'] = '新闻'
            item['source'] = source_str
            item['type'] = None
            item['writer'] = None
            item['pubdate'] = pubdate
            item['tags'] = None
            item['opinion'] = None
            item['remarks'] = None
            item['category_id'] = None
            item['companyremark'] = None
            item['industryremark'] = None
            item['pararremark'] = None
            item['create_date'] = now_date.get_now_time()
            item['uuid'] = uuid.uuid5(uuid.NAMESPACE_DNS, response.url)
            yield item