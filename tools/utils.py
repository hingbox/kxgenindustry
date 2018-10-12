#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : utils.py
@创建时间：2018/8/23 19:43
'''
class Utils(object):

    '''
    这个方法是用来 对访问地址补0
    '''
    def address_zero_fill(self, i):
        if (i>0 and i<10):
            return '00000000'
        elif(i>9 and i<100):
           return'0000000'
        elif (i>99 and i<1000):
            return '000000'
        elif (i>999 and i<10000):
           return '00000'
        elif (i>9999 and i<100000):
            return '0000'
        else:
            return ''

    '''
    处理日期 如果日期中 带有年月日 将年月日 替换为'-'
    '''
    def date_replace_line(self, value):
        if value is not None:
            return value.replace('年', '-').replace('月', '-').replace('日', '-')
        else:
            return None

    '''
    处理日期 如果日期中 带有年月日 将年月日 替换为'-'
    '''
    def date_replace_lines(self, value):
        if value is not None:
            return value.replace('年', '-').replace('月', '-').replace('日', '')
        else:
            return None

    '''
    处理日期 如果日期中 带有'/',替换为'-'
    '''
    def sprit_replace_line(self, value):
        if value is not None:
            return value.replace('/', '-')
        else:
            return None

    '''
    去掉字符串中空格，换行
    '''
    def remove_tnr(self,value):
        if value is not None:
            return value.replace('\r','').replace('\t','').replace('\n','')
        else:
            return None

    '''
    将list转换为str
    '''
    def list_to_str(self,value):
        if value is not None:
            return "".join(value)
        else:
            return None

    '''
    去掉string中空格
    '''
    def str_to_strip(value):
        if value is not None:
            return value.strip()
        else:
            return None

    '''
    字符串中特定文字 替换为空
    '''
    def replace_str_null(self, value, re_value):
        if value is not None:
            return value.replace(re_value, '')
        else:
            return None
    '''
    将'../' 替换为'/'
    '''
    def replace_line_line(self, value, re_value, ls_value):
        if value is not None:
            return value.replace(re_value, ls_value)
        else:
            return None

    '''
    字符串去掉空格，去掉换行，去掉回车，去掉
    '''
    def str_strip_remove_tnr(self, value):
        if value is not None:
            value = value.strip()
            return value.replace('\r','').replace('\t','').replace('\n','')
        else:
            return None