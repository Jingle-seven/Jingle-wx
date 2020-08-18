# coding: utf-8
# 访问我的想读，获取价格

import re, time, string, random, functools
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
           'Cookie': None
           }
RAWHTML = """<html><head>
                <meta charset="UTF-8"> <!-- for HTML5 -->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>开车啦~
            </title></head><body><body/>"""


class WishBook():
    def __init__(self, name=None, author=None):
        self.name = name
        self.author = author
        self.remark = ''
        self.infoDict = dict()
        self.priceList = []
    def __repr__(self):
        return '%s %s %s %s' % (self.name, self.author,len(self.priceList),self.remark)
    def setInfoDict(self,kv):
        self.infoDict = kv
        if '作者' in kv:
            self.author = kv['作者'].replace(' ','').replace('\n','')

class PriceInfo():
    def __init__(self, name=None, publisher=None, year=None, market=None, price=None):
        self.name = name
        self.publisher = publisher
        self.year = year
        self.market = market
        self.price = price

    def __repr__(self):
        return '%s %s %s %s' % (self.name, self.publisher, self.market, self.price)

def getDetailListUrl(wishBookUrl):
    listSoup = bs4.BeautifulSoup(requests.get(wishBookUrl %0, headers=HEADERS).text, "html.parser")
    h1 = listSoup.find_all('h1')[0].stripped_strings
    wishBookNum = re.findall(r'\(\d+\)',list(h1)[0])
    wishBookNum = int(wishBookNum[0][1:-1])
    idxs = list(x*30 for x in range(0,wishBookNum//30 +1))
    print(idxs)
    detailList = []
    for i in idxs:
        time.sleep(1.5)
        listSoup = bs4.BeautifulSoup(requests.get(wishBookUrl % i, headers=HEADERS).text, "html.parser")
        detailListA = listSoup.find_all('a', href=re.compile(r'https://book.douban.com/subject/\d*/'))
        for aTag in detailListA:
            detailList.append(aTag.attrs['href'])
    print(detailList,len(detailList))
    return detailList

# 获取页面中的标题，并进行筛选
def scan30Books(wishBookUrl):
    # print(wishBookUrl)
    HEADERS['Cookie'] = genBid()
    listSoup = bs4.BeautifulSoup(requests.get(wishBookUrl, headers=HEADERS).text, "html.parser")
    if listSoup.prettify().find("403") > 0 or listSoup.prettify().find("302") > 0:
        open("../../resource/errorPage.html", "w", encoding="utf-8").write(listSoup.prettify())
        # print("访问异常")
        HEADERS['Cookie'] = genBid()
    # find_all返回的是tag，name是标签名，attrs是属性字典,text是标签内字符串
    detailUrlList = listSoup.find_all('a', href=re.compile(r'https://book.douban.com/subject/\d*/'))
    for i in range(20, len(detailUrlList)):
        wishBook = WishBook()
        aTag = detailUrlList[i]
        wishBook.name = aTag.get_text().strip()
        print(aTag.name, aTag.get_text().strip(), aTag.attrs)
        time.sleep(1.5)  # 豆瓣爬虫要求的最低间隔为5秒,但据说1秒以上也不会被封
        detailSoup = bs4.BeautifulSoup(requests.get(aTag.attrs['href'], headers=HEADERS).text, "html.parser")
        wishBook.setInfoDict(infoTagToMap(detailSoup.find_all('div', id='info')))
        open("../../resource/errorPage.html", "w", encoding="utf-8").write(detailSoup.prettify())
        allVersionA = detailSoup.find_all('a', href=re.compile(r'https://book.douban.com/works/\d*'))
        if allVersionA:
            wishBook.priceList = getAllVersionPrice(allVersionA[0].attrs['href'])# 各版本各商城价格信息
        else:
            buyInfo = detailSoup.find_all('ul', class_='bs current-version-list')  # 此版本各商城价格信息
            if buyInfo:
                wishBook.remark = str(list(buyInfo[0].stripped_strings)).replace(' ',"").replace('\n','')
            else:
                wishBook.remark = '无价格信息'
        print(wishBook)

# 传入wishBook对象和对应的所有版本URL，获取所有版本的价格信息
def getAllVersionPrice(allVersionUrl):
    priceList = []
    time.sleep(1.5)
    allVersionSoup = bs4.BeautifulSoup(requests.get(allVersionUrl, headers=HEADERS).text, "html.parser")
    versionTags = allVersionSoup.find_all('div', class_='bkses clearfix')
    versionStrs = []
    for v in versionTags:# 提取字符串，稍后统一处理
        versionStrs.append(list(v.stripped_strings))
    for v in versionStrs:
        base = PriceInfo()
        for s in v:
            if s == '(' or s == ')':
                v.remove(s)
        for i in range(0, len(v) - 1):
            if ' ' in v[i] or '\\n' in v[i]:
                v[i] = v[i].replace(' ', '').replace('\n', '')
            if v[i] == '出版社:':
                base.publisher = v[i + 1]
            elif v[i] == '出版年:':
                base.year = v[i + 1]
            elif v[i] == '作者:' and base.name==None: # 书名会在作者前一位，有译者和作者则在译者前一位
                base.name = v[i - 1]
            elif v[i] == '译者:':
                base.name = v[i - 1]
        for i in range(0, len(v) - 1):
            if re.match(r'RMB\d+\.\d+', v[i]):
                priceInfo = PriceInfo(base.name, base.publisher, base.year, v[i - 1], float(v[i].replace('RMB', '')))
                # print(priceInfo)
                priceList.append(priceInfo)
    return priceList

# 根据书本详情页面书本的div获取书本基本信息
def infoTagToMap(infoTag):
    kv = dict()
    strList = []
    rawStrGen = infoTag[0].stripped_strings
    for i in rawStrGen:
        s = i.replace(':', '')
        if s == '':
            continue
        elif s == '/':  # 译者有多个的时候会产生多个值，要合并
            strList[-1] = strList[-1] + '/' + rawStrGen.__next__()
            continue
        strList.append(s)
    # print(len(strList),strList)
    for i in range(0, len(strList), 2):
        kv[strList[i]] = strList[i + 1]
    print(kv)
    return kv

# 获取一个随机的bid，cookie似乎会用到
def genBid(): return "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))


if __name__ == "__main__":
    print("start...")
    wishBookUrl = 'https://book.douban.com/people/71651744/wish?start=%d&mode=list'
    getDetailListUrl(wishBookUrl)
    # scan30Books(wishBookUrl)
    print("end!")
