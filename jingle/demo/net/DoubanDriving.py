# coding: utf-8
# author: xz

import re, time, string, random
import requests, bs4
from concurrent.futures import ThreadPoolExecutor, as_completed

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
           # 'Cookie':open("../../resource/douban_cookie","r").read()
           'Cookie':None
           }
RAWHTML = """<html><head>
                <meta charset="UTF-8"> <!-- for HTML5 -->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>开车啦~
            </title></head><body><body/>"""

# 获取页面中的标题，并进行筛选
def filterPage(groupUrl, start):
    url = groupUrl % start
    discussPage = requests.get(url, headers=HEADERS,allow_redirects=False)
    soup = bs4.BeautifulSoup(discussPage.text, "html.parser")
    if soup.prettify().find("403") > 0 or soup.prettify().find("302") > 0:
        print("访问异常")
        HEADERS['Cookie'] = genBid()
    # find_all返回的是tag，name是标签名，attrs是属性字典,text是标签内字符串
    for i in soup.find_all('a',href=re.compile(r'https://www.douban.com/group/topic/\d*/')):
        # print(type(i))
        # print(i.name,i.attrs)
        detailUrl = i.attrs['href']
        time.sleep(6)  # 豆瓣爬虫要求的最低间隔为5
        detailSoup = bs4.BeautifulSoup(requests.get(detailUrl,headers=HEADERS,allow_redirects=False).text, "html.parser")
        for j in detailSoup.find_all('p',
                                     class_=None,# 回复内容的标签有class，此处过滤掉回复
                                     text=re.compile(r'.*(中山大学|中大|晓港|鹭江|装修).*')):
            print(detailUrl,j.text)
            yield i

# 扫描页面，total是页数，每页25个帖子
def scanPages(groupUrl,total):
    cars = set()
    pageCounter = 0
    pool = ThreadPoolExecutor(max_workers=10)
    # 用getTopicsInPage方法查找符合的内容，start是方法参数
    # 不使用线程池
    # futures = [pool.submit(filterPage, groupUrl, start) for start in range(0, total * 25, 25)]
    # for f in as_completed(futures):
    #   cars.update(set(f.result()))
    for start in range(0, total * 25, 25):
        time.sleep(6)  # 豆瓣爬虫要求的最低间隔为5
        for f in filterPage(groupUrl, start):
            cars.update(set(f))
            pageCounter += 1
            # 阶段性保存
            if pageCounter % 10 == 0:
                print("第%s页" % pageCounter)
                yield cars
                cars.clear()

    return cars


def appendTags(rawSoup,linkTags):
    # rawSoup = bs4.BeautifulSoup(RAWHTML, "html.parser")
    html = rawSoup.html
    for tag in linkTags:
        html.append(tag)
        html.append(rawSoup.new_tag("br"))
    # print(linkTags)
    return rawSoup

def genBid():
    return "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
if __name__ == "__main__":
    print("start...")
    groupUrl = 'https://www.douban.com/group/haizhuzufang/discussion?start=%d'
    rawSoup = bs4.BeautifulSoup(RAWHTML, "html.parser")
    for carTags in scanPages(groupUrl,100):
        resSoup = appendTags(rawSoup,carTags)
        open("../../resource/cars.html", "w", encoding="utf-8").write(resSoup.prettify())
    print("end!")
