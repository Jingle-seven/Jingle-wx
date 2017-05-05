# coding: utf-8
# author: xz

import re,time
import requests, bs4
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Referer': 'https://www.douban.com/',
           'Host': 'www.douban.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
           'Cookie':open("cookie","r").read()
           }

def getTopics(url):
    discussPage = requests.get(url,headers=HEADERS)
    soup = bs4.BeautifulSoup(discussPage.text, "html.parser")
    for i in soup.find_all('a',
                           href=re.compile(r'https://www.douban.com/group/topic/\d{8,9}/'),
                           title=re.compile(r'.{0,20}[夜,车].{0,20}')):
        print(i)


if __name__ == "__main__":
    for i in range(0, 10000, 25):
        if i % 1000 == 0:
            print(i)
        getTopics('https://www.douban.com/group/blabla/discussion?start=%d' % i)
        # time.sleep(6)# 豆瓣设置的最低延迟为5
    print("end")
