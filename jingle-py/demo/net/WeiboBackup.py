# coding=utf-8
import re, time
import requests, bs4

HEADERS = {'Cache-Control': 'no-store',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
           'Cookie': open("../../resource/weibo_cookie", "r").read()}


def getRawMsg(page):
    url = 'http://weibo.com/p/aj/v6/mblog/mbloglist?domain=100505&id=1005053031859063&page=%s' % page
    time.sleep(6)  # 要求的最低延迟为5
    msg = requests.get(url, headers=HEADERS)
    rawData = msg.content.decode("utf-8")
    theData = rawData.encode('utf-8').decode('unicode_escape').replace(' ','')
    print(theData.replace('\n',''))
    reg = re.compile(r'[\u4e00-\u9fa5|,.:()]{5,}')
    regex = re.compile(r'nick-name.+[\u4e00-\u9fa5|,.:()，。：（）|\n|\w]+')
    for i in regex.findall(theData):
        print(i)
    # soup = bs4.BeautifulSoup(rawData, "html.parser")
    # condition = {"class": r'\"WB_text'}
    # for i in soup.find_all('div', condition):
    #     # print(i)
    #     # 处理返回的unicode字符
    #     print(i.text.encode('utf-8').decode('unicode_escape'))
    # return msg.content.decode("utf-8")


class TimeWeiBo:
    def __init__(self, time, weibo):
        self.time = time
        self.weibo = weibo

    def __str__(self):
        return "%s: %s" % (self.time, self.weibo)


if __name__ == '__main__':
    print("start")
    getRawMsg(1)
    print("end")
