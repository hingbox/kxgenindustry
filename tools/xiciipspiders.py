#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：采集西刺的代理ip 并入库，随机获取ip,端口
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : xiciipspiders.py
@创建时间：2018/5/16 0:06
'''
import requests
from scrapy.selector import Selector
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="finance", port=3306, charset="utf8")
cursor = conn.cursor()
#采集西刺免费ip代理
def crawl_ips():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    for i in range(2):
        re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        selector = Selector(text=re.text)
        all_trs = selector.css("#ip_list tr")
        ip_list = []
        for tr in all_trs[1:]:
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split('秒')[0])
            all_text = tr.css("td::text").extract()
            ip = all_text[0]
            port = all_text[1]
            type = all_text[5]
            #speed = float(speed_str.split('秒')[0])
            ip_list.append((ip, port, speed, type))
            #print ('speed_str',speed,all_text[0],all_text[1],all_text[5])
        for ip_info in ip_list:
            # cursor.execute(
            #     "insert into xiciip(ip,port)values('{0}','{1}')",
            #     (ip_info[0],ip_info[1])
            #
            # )
            cursor.execute("insert into xiciip(ip,port,type,speed) values (%s,%s,%s,%s)",\
                          (ip_info[0], ip_info[1], ip_info[3], ip_info[2]))
            conn.commit()

#采集快代理免费ip
def crawl_kuaidaili_ips():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    for i in range(2):
        re = requests.get("https://www.kuaidaili.com/free/inha/{0}".format(i), headers=headers)
        selector = Selector(text=re.text)
        all_trs = selector.css("#ip_list tr")
        ip_list = []
        for tr in all_trs[1:]:
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split('秒')[0])
            all_text = tr.css("td::text").extract()
            ip = all_text[0]
            port = all_text[1]
            type = all_text[5]
            #speed = float(speed_str.split('秒')[0])
            ip_list.append((ip, port, speed, type))
            #print ('speed_str',speed,all_text[0],all_text[1],all_text[5])
        for ip_info in ip_list:
            # cursor.execute(
            #     "insert into xiciip(ip,port)values('{0}','{1}')",
            #     (ip_info[0],ip_info[1])
            #
            # )
            cursor.execute("insert into xiciip(ip,port,type,speed) values (%s,%s,%s,%s)",\
                          (ip_info[0], ip_info[1], ip_info[3], ip_info[2]))
            conn.commit()

'''
获取代理ip类
'''
class GetIp(object):
    '''
    根据ip 删除不可用的ip
    '''
    def delete_ip(self, ip):
        delete_sql = """
                delete from xiciip where ip='{0}'
          """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    '''
    根据pi，端口 判断代理ip是否可用
    '''
    def judge_ip(self, ip, port):
        http_url ="http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip,port)
        try:
            proxy_dict = {
                "http": proxy_url
            }
            response = requests.get(http_url,proxies=proxy_dict)
        except Exception as e:
            print('invalid ip and port')
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >=200 and code < 300:
                print('effective ip')
                return True
            else:
                print('invalid ip')
                self.delete_ip(ip)
                return False

    '''
    从数据库中随机获取ip
    '''
    def get_random_ip(self):
        random_sql = """
                  select ip,port from xiciip order by RAND() limit 1
        """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            judge_re = self.judge_ip(ip, port)
            if judge_re:
                return "http://{0}:{1}".format(ip, port)
            else:
                return self.get_random_ip()

#print (crawl_ips())
if __name__ == "__main__":
    get_ip = GetIp()
    get_ip.get_random_ip()