# 用于下载某个豆瓣影人的所有图片
# 2018.1.27 未完成
# 需解决的问题：urlretrieve 403 forbidden
# 参考链接：http://blog.csdn.net/cquptcmj/article/details/53526137

from urllib import request
import re

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Referer': 'https://www.douban.com/',
           'Host': 'www.douban.com',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

actorUrl = "https://movie.douban.com/celebrity/1275342/"
actorImgsUrl = "https://movie.douban.com/celebrity/1275342/photos/"
actorImg = "https://img3.doubanio.com/view/photo/raw/public/p2209122376.jpg"

"""
https://img3.doubanio.com/view/photo/raw/public/p2209122376.jpg
https://movie.douban.com
"""
req = request.Request(actorImg, headers=HEADERS)
request.urlretrieve(actorImg, "G:/xunlei/net-photo/douban" + actorImg[-10:])