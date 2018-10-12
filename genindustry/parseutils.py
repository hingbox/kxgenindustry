#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：这个是解析页面的工具类
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : parseutils.py
@创建时间：2018/5/10 21:13
'''
class ParseUtils(object):
    '''
    传入三个参数
    response 响应体(必传参数)
    first_tag html第一个要解析的标签(必传参数)
    class_id 传入class或者是id(必传参数)
    class_id_name 传入class或者是id的name(必传参数)
    first_tag html最后一个要解析的标签(选填参数)
    '''
    def parse_li_lists(self, response, first_tag, class_id, class_id_name, last_tag):
        if response is not None:
        #response.xpath('//'+first_tag+'[@'+class_id+'='+class_id_name+']/'+last_tag)
            if last_tag is not None:
                temp = '//'+first_tag+'[@'+class_id+'="'+class_id_name+'"]/'+last_tag
            else:
                temp = '//'+first_tag+'[@'+class_id+'="'+class_id_name+'"]'
            return response.xpath(temp)
        else:
            return None