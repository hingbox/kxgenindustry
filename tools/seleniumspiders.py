#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : seleniumspiders.py
@创建时间：2018/5/16 16:52
'''
from selenium import webdriver
from scrapy.selector import Selector
browser = webdriver.Chrome(executable_path="d:/Tools/chromedriver_win32/chromedriver.exe")
# browser.get("http://www.baidu.com")
# t_selector = Selector(text=browser.page_source)
# print(t_selector.xpath('//div[@id="u1"]/a[1]/text()').extract()[0])

#模拟知乎登录
# browser.get("https://www.zhihu.com/signup")
# browser.find_element_by_css_selector(".Login-content input[name='username']").send_keys("")
# browser.find_element_by_css_selector(".Login-content input[name='password']").send_keys("")
# browser.find_element_by_css_selector('.Button .SignFlow-submitButton .Button--primary .Button--blue').click()
###browser.quit()

#selenium 集成scrapy
#1、selenium获取页面元素
# browser = webdriver.Chrome(executable_path="D:/browserexe/chromedriver.exe")
# browser.get("https://item.taobao.com/item.htm?spm=a310p.7395725.1998460392.1.ffca6c0NXDhB5&id=549869514793") #运行浏览器
# page_source = browser.page_source  #相当于“浏览器f12”，普通爬虫获取的源码是相当于直接获取网页源码，所以js动态添加的内容不会被获取到，但是通过这种方式f12，会获取到js动态添加的
# t_selector = Selector(text=page_source)#页面元素提取能用scrapy尽量用，不能用在用selenium，因为scrapy速度更快
# print(t_selector.css('#J_PromoPriceNum::text').extract_first()) #获取页面js动态添加上去的价格
# browser.quit()


#2、selenium模拟知乎登陆
# browser = webdriver.Chrome(executable_path="D:/browserexe/chromedriver.exe")
# browser.get("https://www.zhihu.com/#signin")
# browser.find_element_by_css_selector('.signin-switch-password').click() #点击使用密码登陆
# browser.find_element_by_name('account').send_keys('username') #输入账号
# browser.find_element_by_name('password').send_keys('password')#输入密码
# time.sleep(6) #等待输入验证码
# browser.find_element_by_css_selector(".view-signin button.sign-button").click()
# browser.quit()


#3、selenium模拟微博登陆
# browser = webdriver.Chrome(executable_path="D:/browserexe/chromedriver.exe")
# browser.get("http://weibo.com/login.php")
# time.sleep(2)#防止页面未加载完成，就直接去查找元素找不到的情况
# browser.find_element_by_id('loginname').send_keys('13247629622')
# browser.find_element_by_css_selector('.info_list .input_wrap  input[name="password"]').send_keys('lxj546630576.')
# browser.find_element_by_css_selector('.info_list a[action-type="btn_submit"]').click()
# #鼠标下滑加载
# for i in range(3): #下滑三次
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight);var leftOfPage = document.body.scrollHeight;return leftOfPage;') #执行js代码
#     time.sleep(2)


#4、设置selenium不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="D:/browserexe/chromedriver.exe",chrome_options=chrome_opt)
# browser.get("https://www.taobao.com")


#5、phantomjs（不推荐使用）, 无界面的浏览器， 多进程情况下phantomjs性能会下降很严重
#下载phantomjs驱动
# browser = webdriver.PhantomJS(executable_path="D:/browserexe/phantomjs.exe")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")
# print (browser.page_source)
# browser.quit()


#6、将selenium集成scrapy中
#6.1 middlewares中添加
from scrapy.http import HtmlResponse
class JSPageMiddleware(object):

    #通过chrome请求动态网页
    def process_request(self, request, spider):
        if spider.name == "jobbole":
            # browser = webdriver.Chrome(executable_path="D:/Temp/chromedriver.exe")
            spider.browser.get(request.url)
            import time
            time.sleep(3)
            print ("访问:{0}".format(request.url))
            #不需要放到下载器，去下载页面，直接renturn
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8", request=request)
#6.2 spiders中添加
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals

# def __init__(self):
      # 初始化时候，给爬虫新开一个浏览器
#       self.browser = webdriver.Chrome(executable_path="D:/Temp/chromedriver.exe")
#       super(JobboleSpider, self).__init__()
#       dispatcher.connect(self.spider_closed, signals.spider_closed)#第二个参数是信号（spider_closed:爬虫关闭信号，信号量有很多）,第一个参数是当执行第二个参数信号时候要执行的方法
#
#   def spider_closed(self, spider):
#       #当爬虫退出的时候关闭chrome
#       print ("spider closed")
#       self.browser.quit()


#7、不显示浏览器界面（不作为重点）
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))  #visible浏览器不显示,windows下不支持，如果出错“no such file or directory”:pip install xvfbwrapper(xvfb)
# display.start()
#
# browser = webdriver.Chrome()
# browser.get()



#python+selenium+scrapy搭建简单爬虫
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.selector import Selector
import time
import os

def writeFile(dirPath, page):
    data = Selector(text = page).xpath("//td[@class='zwmc']/div/a")
    titles = data.xpath('string(.)').extract()
    timeMarks = Selector(text = browser.page_source).xpath("//td[@class='gxsj']/span/text()").extract()
    links = Selector(text = browser.page_source).xpath("//td[@class='zwmc']/div/a/@href").extract()

    for i in range(len(titles)):
        fileName = titles[i].replace(':', '-').replace('/', '-').replace('\\', '-').replace('*', 'x').replace('|', '-').replace('?', '-').replace('<', '-').replace('>', '-').replace('"', '-').replace('\n', '-').replace('\t', '-')
        filePath = dirPath + os.sep + fileName + '.txt'

        with open(filePath, 'w') as fp:
            fp.write(titles[i])
            fp.write('$***$')
            fp.write(timeMarks[i])
            fp.write('$***$')
            fp.write(links[i])


def searchFunction(browser, url, keyWord, dirPath):
    browser.get(url)

#勾选城市
    browser.find_element_by_xpath("//input[@id='buttonSelCity']").click()
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[1]/td/label/input[@iname='北京']").click()
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[1]/td/label/input[@iname='上海']").click()
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[3]/td/label/input[@iname='南京']").click()
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[4]/td/label/input[@iname='苏州']").click()
    browser.find_element_by_xpath("//table[@class='sPopupTabC']/tbody/tr[4]/td/label/input[@iname='无锡']").click()
    browser.find_element_by_xpath("//div[@class='sPopupTitle250']/div/a[1]").click()

#定位搜索框
    searchBox = browser.find_element_by_xpath("//div[@class='keyword']/input[@type='text']")

#发送搜索内容
    searchBox.send_keys(keyWord)

#确认搜索
    browser.find_element_by_xpath("//div[@class='btn']/button[@class='doSearch']").click()

    totalCount = Selector(text = browser.page_source).xpath("//span[@class='search_yx_tj']/em/text()").extract()[0]
    pageOver = int(totalCount) / 40
    for i in range(pageOver):
        time.sleep(3)
        writeFile(dirPath, browser.page_source)
        browser.find_element_by_link_text("下一页").click()

    time.sleep(3)
    writeFile(dirPath, browser.page_source)


if __name__ == '__main__':
    print 'START'
    url = 'http://www.zhaopin.com/'
    keyWord = u"华为技术有限公司"
    dirPath = keyWord + u"招聘信息"

    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

#定义一个火狐浏览器对象
    browser = webdriver.Chrome(executable_path="d:/Tools/chromedriver_win32/chromedriver.exe")
    searchFunction(browser, url, keyWord, dirPath)

    browser.close()
    print 'END'
