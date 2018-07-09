from urllib import request
import re

def write():
    url = "http://www.bing.com/"
    web_data = request.urlopen(url).read()
    print(web_data)
    output = open("page.html","w", encoding="utf-8")
    output.write(web_data.decode("utf-8"))
    output.close()

print("开始写入")
write()
print("写入完成")