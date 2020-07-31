# coding: utf-8
# 访问我的想读，获取价格

import re, time, string, random
import requests, bs4

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Referer': 'https://www.douban.com/',
           'Host': 'book.douban.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
           # 'Cookie':open("../../resource/douban_cookie.txt","r").read()
           'Cookie':None
           }
RAWHTML = """<html><head>
                <meta charset="UTF-8"> <!-- for HTML5 -->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>开车啦~
            </title></head><body><body/>"""

# 获取页面中的标题，并进行筛选
def scan30Books(wishBookUrl, start):
    wishBookUrl = wishBookUrl % start
    print(wishBookUrl)
    HEADERS['Cookie'] = genBid()
    listPage = requests.get(wishBookUrl, headers=HEADERS,allow_redirects=False)
    listSoup = bs4.BeautifulSoup(listPage.text, "html.parser")
    if listSoup.prettify().find("403") > 0 or listSoup.prettify().find("302") > 0:
        open("../../resource/errorPage.html", "w", encoding="utf-8").write(listSoup.prettify())
        # print("访问异常")
        HEADERS['Cookie'] = genBid()
    # find_all返回的是tag，name是标签名，attrs是属性字典,text是标签内字符串
    detailUrlList = listSoup.find_all('a',href=re.compile(r'https://book.douban.com/subject/\d*/'))
    for i in range(0,5):
        aTag = detailUrlList[i]
        # print(type(aTag))
        print(aTag.name,aTag.get_text().strip(),aTag.attrs)
        detailUrl = aTag.attrs['href']
        time.sleep(6)  # 豆瓣爬虫要求的最低间隔为5秒
        detailSoup = bs4.BeautifulSoup(requests.get(detailUrl,headers=HEADERS,allow_redirects=False).text, "html.parser")
        infoDiv  = detailSoup.find_all('div',id='info')
        # infoTagToMap(infoDiv)
        buyInfo1 = detailSoup.find_all('ul',class_='bs current-version-list') # 各商城价格信息
        buyInfo2 = detailSoup.find_all('ul', class_='secondhand-books-list bs')# 二手价格信息
        # print([x for x in buyInfo1[0].stripped_strings])
        print(len(buyInfo1),len(buyInfo2))
        # buyInfoToMap(buyInfo1[0])
        for x in buyInfo2:
            # print(x.prettify())
            buyInfoToMap(x)

def infoTagToMap(infoTag):
    kv = dict()
    # print(len(infoTag[0].contents))
    # for span in infoTag[0].contents:
    #     if span == '\n' or type(span) ==bs4.element.NavigableString:
    #         continue
    #     elif span.name == 'span':
    #         print(span.string,span.get_text())
    #         print(repr(str(span)).replace("'", ""))
    strList = []
    rawStrGen = infoTag[0].stripped_strings
    for i in rawStrGen:
        s = i.replace(':','')
        if s == '':
            continue
        elif s == '/': # 译者有多个的时候会产生多个值，要合并
            strList[-1] = strList[-1] + '/' + rawStrGen.__next__()
            continue
        strList.append(s)
    # print(len(strList),strList)
    for i in range(0,len(strList),2):
        kv[strList[i]] = strList[i+1]
    print(kv)
    return kv
def buyInfoToMap(buyInfoTag):
    marketToPrice = buyInfoTag.find_all('div',class_=re.compile('cell price-btn-wrapper|flex-wrap'))
    for i in marketToPrice:
        print([x for x in i.stripped_strings])

    return {}

def genBid():
    # bid=BrtMW0YyQ8l
    return "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
if __name__ == "__main__":
    print("start...")
    wishBookUrl = 'https://book.douban.com/people/71651744/wish?start=%d&mode=list'
    scan30Books(wishBookUrl,0)
    # print(genBid())
    # rawSoup = bs4.BeautifulSoup(RAWHTML, "html.parser")
    # resSoup = appendTags(rawSoup,[])
    # open("../../resource/cars.html", "w", encoding="utf-8").write(resSoup.prettify())
    print("end!")
