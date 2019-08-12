# coding: utf-8
# author: xz

from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time
import requests

class Page:
    def __init__(self):
        self.url=None
        pass
    def cBack(self,future):
        self.url = future.result().url
        print(self.url)
        return self.url

URLS = ['http://sina.com', 'http://www.baidu.com','http://www.163.com', 'http://qq.com', ]
def task(url, timeout=10):
    return requests.get(url, timeout=timeout)

pool = ThreadPoolExecutor(max_workers=10)
futures = [pool.submit(task, url) for url in URLS]


# 回调函数,异步返回,不会阻塞主线程
# for i in futures:
#     page = Page()
#     i.add_done_callback(page.cBack)
#     print(page.url)  # 然而执行到这里请求还未返回, 所以是空


# 异步执行, 会阻塞主线程
for i in as_completed(futures):
    print('%s, done, result: %s' % (i.result().url, len(i.result().content)))
# 同步执行, 会阻塞主线程
# for i in futures:
#     print('%s, done, result: %s' % (i.result().url, len(i.result().content)))

print("请求发送完成")