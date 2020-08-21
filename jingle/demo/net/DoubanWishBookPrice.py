# coding: utf-8
# 访问我的想读，获取价格

import re, time, string, random, functools
import requests, bs4,openpyxl
import jingle.demo.work.SkData as SkData

# 获取一个随机的bid，cookie似乎会用到
def genBid(): return "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
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
           'Cookie': genBid()
           }
RAWHTML = """<html><head>
                <meta charset="UTF-8"> <!-- for HTML5 -->
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>开车啦~
            </title></head><body><body/>"""
sleepTime = 2
timeStr = time.strftime("%Y-%m-%d %H:%M", time.localtime())
class WishBook():
    def __init__(self, name=None, author=None):
        self.name = name
        self.author = author
        self.remark = ''
        self.infoDict = dict()
        self.priceList = []
    def __repr__(self):
        return '%s|%s|版本价格数量%s|%s' % (self.name, self.author,len(self.priceList),self.remark)
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

# 在我想看的书页面获取所有书本的链接
def getDetailUrlList(wishBookUrl):
    listSoup = bs4.BeautifulSoup(requests.get(wishBookUrl %0, headers=HEADERS,allow_redirects=False).text, "html.parser")
    open("../../resource/errorPage.html", "w", encoding="utf-8").write(listSoup.prettify())
    h1 = listSoup.find_all('h1')[0].stripped_strings
    wishBookNum = re.findall(r'\(\d+\)',list(h1)[0])
    print(wishBookNum)
    wishBookNum = int(wishBookNum[0][1:-1])
    idxs = list(x*30 for x in range(0,wishBookNum//30 +1))
    print(idxs)
    detailList = []
    for i in idxs:
        time.sleep(sleepTime)
        listSoup = bs4.BeautifulSoup(requests.get(wishBookUrl % i, headers=HEADERS,allow_redirects=False).text, "html.parser")
        detailListA = listSoup.find_all('a', href=re.compile(r'https://book.douban.com/subject/\d*/'))
        for aTag in detailListA:
            detailList.append(aTag.attrs['href'])
    print(len(detailList),detailList)
    return detailList

# 扫描一本书
def scanBookUrl(wishBookUrl):
    wishBook = WishBook()
    time.sleep(sleepTime)  # 豆瓣爬虫要求的最低间隔为5秒,但据说1秒以上也不会被封
    detailSoup = bs4.BeautifulSoup(requests.get(wishBookUrl, headers=HEADERS,allow_redirects=False).text, "html.parser")
    wishBook.name = detailSoup.find_all('h1')[0].stripped_strings.__next__()
    wishBook.setInfoDict(infoTagToMap(detailSoup.find_all('div', id='info')))
    # open("../../resource/errorPage.html", "w", encoding="utf-8").write(detailSoup.prettify())
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
    return wishBook

# 传入wishBook对象和对应的所有版本URL，获取所有版本的价格信息
def getAllVersionPrice(allVersionUrl):
    priceList = []
    time.sleep(sleepTime)
    allVersionSoup = bs4.BeautifulSoup(requests.get(allVersionUrl, headers=HEADERS,allow_redirects=False).text, "html.parser")
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
    priceList.sort(key=lambda x:x.price) # 排序，钱少的在前面
    # for x in priceList: print(x)
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
    # print(kv)
    return kv
def writeExcel(wishBooks):
    # print(wishBooks)
    wbook = openpyxl.Workbook()
    sheet = wbook.worksheets[0]
    sheet.append(['书名(16)','作者(10)','价格1(20)','价格2(20)','价格3(20)','价格4(20)','价格5(20)','最高价(20)','备注'])
    for b in wishBooks:
        # p = list("='%s'&CHAR(10)&'%s'&CHAR(10)&'%s'"%(x.price,x.publisher,x.market) for x in b.priceList)
        p = list("%s|\n%s|\n%s" % (x.price, x.publisher, x.market) for x in b.priceList)
        print(p)
        while len(p)<5:
            p.insert(len(p)-1,'')
        sheet.append([b.name,b.author,p[0],p[1],p[2],p[3],p[4],p[len(p)-1],b.remark])
    SkData.setBorderWidth(sheet)
    wbook.save('../../resource/doubanWishBookPrice%s.xlsx'%timeStr)



if __name__ == "__main__":
    print("start...")
    uids = ['71651744','66803432']
    wishBookList = []
    wishBookUrl = 'https://book.douban.com/people/'+uids[2]+'/wish?start=%d&mode=list'
    detailUrlList = getDetailUrlList(wishBookUrl)
    for i in detailUrlList:
        wishBookList.append(scanBookUrl(i))
    # wishBookList.append(scanBookUrl(detailUrlList[0]))
    writeExcel(wishBookList)
    print("end!")
