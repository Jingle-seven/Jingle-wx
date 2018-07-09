import random
import re, time
import string

import requests, bs4

# 测试目录页面
def getAll():
    url = 'https://www.douban.com/group/haizhuzufang/discussion?start=0'
    time.sleep(6)  # 豆瓣爬虫要求的最低间隔为5
    discussPage = requests.get(url)
    soup = bs4.BeautifulSoup(discussPage.text, "html.parser")
    if soup.prettify().find("403 Forbidden") > 0:
        print("禁止访问403")
    for i in soup.find_all('a',href=re.compile(r'https://www.douban.com/group/topic/\d*/')):
        # print(type(i))
        # print(i.name,i.attrs)
        detailUrl = i.attrs['href']
        detailSoup = bs4.BeautifulSoup(requests.get(detailUrl).text, "html.parser")
        for j in detailSoup.find_all('p',
                                     class_=None,# 回复内容的标签有class，此处过滤掉回复
                                     text=re.compile(r'.*(中山大学|中大|晓港|鹭江).*')):
            print(detailUrl)
            print("\t",j.text)
    print("END")

# 测试细节页面
def getP():
    url = 'https://www.douban.com/group/topic/114162360/'
    detailSoup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    for j in detailSoup.find_all('p',class_=None):
        print("\t",j.text)

    print('----------------------------->')
    #
    for j in detailSoup.find_all('p',text=re.compile(r'.*(中山大学|中大|晓港|鹭江|不限).*')):
        print("\t",j.text)

# getAll()
# getP()
# 从abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789中选11个字符
s = "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
# print(s)
s2 = random.sample(['1','2','3','4','5'],3)
print("A".join(s2))