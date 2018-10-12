#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：根据url返回对应的网站名称
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : geturlbyname.py
@创建时间：2018/7/21 22:32
'''
class GetUrlByName(object):

    def get_type_from_url(self, url):
        if 'anhui' in url:
            return u'安徽网事'
        elif 'szyw' in url:
            return u'时政要闻'
        elif 'society' in url:
            return u'社会'
        elif 'youth' in url:
            return u' 共青团讯'
        elif 'qpeople' in url:
            return u'人物'
        elif 'qnlt' in url:
            return u'青年之声'
        elif 'edu' in url:
            return u'教育'
        elif 'ahjyxclm' in url:
            return u'安徽教育宣传联盟'
        elif 'finance' in url:
            return u'财经'
        elif 'photo' in url:
            return u'图片新闻'
        elif 'business' in url:
            return u'商 '
        elif 'ds' in url:
            return u'文化'
        elif 'ty' in url:
            return u'体育'
        elif 'auto' in url:
            return u'汽车'
        elif 'fashion' in url:
            return u'时尚'
        elif 'health' in url:
            return u'健康'
        elif 'yl' in url:
            return u'娱乐'
        elif 'ly' in url:
            return u'旅游'
        else:
            return ''


    def get_type_from_guangzhou_url(self, url):
        if 'caijing' in url:
            return u'财经'
        elif 'keji' in url:
            return u'科技'
        elif 'jiaoyu' in url:
            return u'教育'
        elif 'zixun' in url:
            return u' 资讯'
        elif 'shangye' in url:
            return u'商业'
        elif 'chexun' in url:
            return u'车讯'
        elif 'jiankang' in url:
            return u'健康'
        elif 'yule' in url:
            return u'娱乐'
        elif 'lvyou' in url:
            return u'旅游'
        else:
            return ''


    def get_type_from_yw_url(self, url):
        if 'jinan' in url:
            return u'济南'
        elif 'shandong' in url:
            return u'山东'
        elif 'guonei' in url:
            return u'要闻'
        elif 'shehui' in url:
            return u' 社会'
        elif 'yule' in url:
            return u'文娱'
        elif 'tiyu' in url:
            return u'体育'
        elif 'redian' in url:
            return u'热点'
        elif 'jiankang' in url:
            return u'健康'
        elif 'caijing' in url:
            return u'财经'
        elif 'fangchan' in url:
            return u'房产'
        elif 'more2' in url:
            return u'国内'
        elif 'more' in url:
            return u'国际'
        elif 'guoji' in url:
            return u'国际新闻'
        elif 'yuanchuang' in url:
            return u'齐鲁原创'

        else:
            return ''

    def return_current_url(self, url):
        if 'guoneixinwen' in url:
            return 'http://www.dzwww.com/xinwen/guoneixinwen'
        else:
            return 'http://www.dzwww.com/xinwen/guojixinwen'

    def get_type_from_dazong_url(self, url):
        if 'guoneixinwen' in url:
            return u'国内新闻'
        else:
            return u'国际新闻'
    #山东新闻
    def get_type_from_shandong_url(self, url):
        if '1228' in url:
            return u'国内新闻'
        elif '1227' in url:
            return u'山东新闻'
        elif '1229' in url:
             return u'国际新闻'
        elif '2215' in url:
            return u'山东各地'
        elif '220' in url:
            return u'社会新闻'
        else:
            return u'天天评论'

    #西部网
    def get_type_from_xibuwang_url(self, url):
        if '4122' in url:
            return u'国内新闻'
        elif '4124' in url:
            return u'社会'
        else:
            return u'国际新闻'

    #神州学人
    def get_type_from_shenzhou_url(self, url):
        if 'ssyl' in url:
            return u'要闻'
        # elif '4124' in url:
        #     return u'社会'
        else:
            return u'国际新闻'

    #时代财经
    def get_type_from_shidaicaijing_url(self, url):
        if 'financeroll' in url:
            return u'财经-滚动'
        elif 'stock' in url:
            return u'财经-股市'
        elif 'yejie' in url:
            return u'科技-业界'
        elif 'net' in url:
            return u'科技-网络'
        elif 'shopping' in url:
            return u'财经-消费'
        else:
            return u'国际新闻'

    #中国攀枝花网
    def get_type_from_panzhihuawang_url(self, url):
        if 'sichuan' in url:
            return u'http://www.pzh.gov.cn'
        elif 'stock' in url:
            return u'财经-股市'
        elif 'yejie' in url:
            return u'科技-业界'
        elif 'net' in url:
            return u'科技-网络'
        elif 'shopping' in url:
            return u'财经-消费'
        else:
            return u'国际新闻'

    #咸宁新闻网
    def get_type_from_xnxww_url(self, url):
        if 'xnxw' in url:
            return u'http://news.xnnews.com.cn/xnxw/'
        elif 'xwjj_1' in url:
            return u'http://news.xnnews.com.cn/xwjj_1/'
        elif 'szxw2' in url:
            return u'http://news.xnnews.com.cn/szxw2/'
        elif 'shxw' in url:
            return u'http://news.xnnews.com.cn/shxw/'
        elif 'msxw2' in url:
            return u'http://news.xnnews.com.cn/msxw2/'
        elif 'xyxw' in url:
            return u'http://news.xnnews.com.cn/xyxw/'
        elif 'snxw' in url:
            return u'http://news.xnnews.com.cn/snxw/'
        elif 'gnxw2' in url:
            return u'http://news.xnnews.com.cn/gnxw2/'
        elif 'gjxw2' in url:
            return u'http://news.xnnews.com.cn/gjxw2/'
        elif 'ylxw' in url:
            return u'http://news.xnnews.com.cn/ylxw/'
        elif 'tyxw_2109' in url:
            return u'http://news.xnnews.com.cn/tyxw_2109/'
        else:
            return u'http://news.xnnews.com.cn/'

