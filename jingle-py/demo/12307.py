import urllib.request
import re
import datetime
from datetime import timedelta
import ctypes
import winsound
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#此程序来自网络
def search(fromDate, toDate):
    found = False
    while not found:
        date = fromDate
        showOneTime = False
        while (date <= toDate):
            url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=' + date.strftime(
                '%Y-%m-%d') + '&from_station=GZQS&to_station=NCQ'
            print(url)
            text = urllib.request.urlopen(url).read().decode('utf-8')
            print(text)
            regular = r'yz_num":"(\d+)'  ##yz_num指的是硬座的数量，其它座类似
            seat_num = re.search(regular, text)
            if seat_num:
                found = True
                print(date, '有票')
                if not showOneTime:
                    showOneTime = True
                    winsound.Beep(2007, 6000)
                    ctypes.windll.user32.MessageBoxW(0, '快去改签,', '有票啦!', 0)
            date = date + timedelta(days=1)


fromM, fromD, toM, toD = 1, 20, 1, 23
str = '正在查找从%d月%d号到%d月%d号是否有从泉州到北京的票...' % (fromM, fromD, toM, toD)
print(str)
search(datetime.date(2015, fromM, fromD), datetime.date(2017, toM, toD))
input()
