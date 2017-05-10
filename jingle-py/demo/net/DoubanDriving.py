# coding: utf-8
# author: xz

import re, time
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
           'Cookie':open("cookie","r").read()
           }
RAWHTML = """<html><head>
                <meta charset="UTF-8"> <!-- for HTML5 -->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>开车啦~
            </title></head><body><body/>"""


def getTopicsInPage(start):
    url = 'https://www.douban.com/group/blabla/discussion?start=%d' % start
    time.sleep(6)  # 要求的最低延迟为5
    discussPage = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(discussPage.text, "html.parser")
    if soup.prettify().find("403 Forbidden") > 0:
        print("禁止访问403")
    for i in soup.find_all('a',
                           href=re.compile(r'https://www.douban.com/group/topic/\d{8,9}/'),
                           title=re.compile(r'.{0,20}[车].{0,20}')):
        print(i)
        yield i


def scanPages(total):
    cars = []
    pageCounter = 0
    pool = ThreadPoolExecutor(max_workers=10)
    futures = [pool.submit(getTopicsInPage, start) for start in range(0, total * 25, 25)]
    for f in as_completed(futures):
        cars.extend(list(f.result()))
        pageCounter += 1
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


if __name__ == "__main__":
    print("start...")
    rawSoup = bs4.BeautifulSoup(RAWHTML, "html.parser")
    for carTags in scanPages(1000):
        resSoup = appendTags(rawSoup,carTags)
        open("cars.html", "w", encoding="utf-8").write(resSoup.prettify())
    print("end!")
