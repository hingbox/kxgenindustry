# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
from MySQLdb.cursors import DictCursor
class GenindustryPipeline(object):
    def __init__(self):
        self.count = 1
        self.dbpool = adbapi.ConnectionPool("MySQLdb",
                                           #host="118.25.35.43",
                                           #port="3306",
                                           db = "scrapydata",      # 数据库名
                                           user = "root",       # 数据库用户名
                                           passwd = "root",     # 密码
                                           cursorclass = DictCursor,
                                           charset = "utf8",
                                           #use_unicode = False,
                                           use_unicode=True,
                                           )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        self.count = self.count + 1

        tb.execute("insert into news (title,type,content,writer,source,sourcecategory,pubdate,create_date,orgurl,tags,opinion,summary,remarks,category_id,companyremark,industryremark,pararremark,uuid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
            (item["title"],item["type"],\
            item["content"],item["writer"],\
            item["source"],item["sourcecategory"],\
            item["pubdate"],item["create_date"],\
            item["orgurl"],item["tags"],\
            item["opinion"],item["summary"],\
            item["remarks"],item['category_id'],\
            item['companyremark'],item['industryremark'],\
            item['pararremark'],item['uuid']))
        print ('---save success---',str(self.count))
        # uuid = item['uuid']
        # if uuid:
        #     tb.execute("select * from news where uuid=%s",uuid)
        #     result=tb.fetchone()
        #     if result is not None:
        #         print('重复数据不保存')
        #         pass
        #     else :
        #          print ('---save success---',str(self.count))
        #          tb.execute("insert into news (title,type,writer,source,orgurl,summary,pubdate,create_date,content,sourcecategory,source_from,uuid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
        #             (item["title"],item["type"],\
        #             item["writer"],item["source"],\
        #             item["orgurl"],item['summary'],\
        #             item['pubdate'],item['create_date'],\
        #             item['content'],item['sourcecategory'],\
        #             item['source_from'],item['uuid']))



    def handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
        print failue
