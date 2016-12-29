from urllib import request

from demo import CatchImgs
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = '''https://kyfw.12306.cn/otn/lcxxcx/query
        ?purpose_codes=ADULT
        &queryDate=2017-01-21
        &from_station=GZQ
        &to_station=NCQ'''

url2 = '''https://kyfw.12306.cn/otn/leftTicket/queryA
       ?leftTicketDTO.train_date=2017-01-21
       &leftTicketDTO.from_station=GZQ
       &leftTicketDTO.to_station=NCQ
       &purpose_codes=ADULT'''

myHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Referer': 'https://kyfw.12306.cn/otn/lcxxcx/init',
    'Host': 'kyfw.12306.cn',
    "Cookie": "JSESSIONID=BD9CA4CF760674EBC0CC1361CD75BB61; " \
              "current_captcha_type=Z; _jc_save_toDate=2016-12-22;" \
              " BIGipServerotn=1373176074.50210.0000;" \
              " _jc_save_fromStation=%u5E7F%u5DDE%2CGZQ;" \
              " _jc_save_toStation=%u5357%u96C4%2CNCQ;" \
              " _jc_save_fromDate=2017-01-20;" \
              " _jc_save_wfdc_flag=dc",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, lzma, sdch, br",
    "Accept - Language": "zh-CN, zh;q = 0.8",
    "Cache-Control": "no - cache",
    "Connection": "keep-alive",
    "If-Modified-Since": "0",
    "X-Requested-With": "XMLHttpRequest"
}
req = request.Request(url, data=None, headers=myHeaders)
resp = request.urlopen(url).read()
trainData = resp.decode('utf-8')
print(trainData)
