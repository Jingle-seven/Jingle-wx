from urllib import request
import re

def write():
    url = "http://www.bing.com/"
    webdata = request.urlopen(url).read()
    output = open("page.html", "w")
    output.write(webdata)
    output.close()

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
   # print(page.getcode())
    return html

def getUrls(page):
    str = r'http.{0,20}.gduf.{0,30}.cn.{0,10}/.{0,10}/|n'
    str1 = r'http.{1,20}.gduf.{0,30}.cn.{0,10}[/n]'
    str2 = r'http://vbird.dic.ksu.edu.tw/linux_basic/.{0,10}.php'
    reg = re.compile(str2)
    pageStr = page.decode('utf-8')
    print(reg.match(""))
    #print(pageStr)
    urlList = re.findall(reg,pageStr)
    return urlList

page = getHtml("http://vbird.dic.ksu.edu.tw/linux_basic/linux_basic.php")
urlList = getUrls(page)
urlSet = set(urlList)
print(len(urlList))
print(len(urlSet))
count = 0;
for url in urlSet:
    try:
        print(url.replace("/","|"))
        request.urlretrieve(url,"G:/temp/pages/%s.html"%count)
        count = count +1
    except OSError as e:
        pass
        print(e)
