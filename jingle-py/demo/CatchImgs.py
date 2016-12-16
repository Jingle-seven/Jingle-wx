from urllib import request
import re

def getHtmlBytes(url):
    req = request.Request(url)
    req.add_header("Mozilla/5.0 (Windows NT 6.1; WOW64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81")
    webData = request.urlopen(url).read()
    #print(webData)
    return webData

def getInnerUrls(pageData,urlPatern):
    reg = re.compile(urlPatern)
    pageStr = pageData.decode('utf-8')
    urlList = re.findall(reg,pageStr)
    return urlList

def getImgInUrls(urlSet,path="G:/temp/pages/"):
    print(len(urlSet))
    for imgUrl in urlSet:
        try:
            print("imgUrl:"+imgUrl)
            request.urlretrieve(imgUrl,path+imgUrl[-10:])
        except OSError as e:
            print(e)

def getImgsFromUrl(baseUrl,urlPatern,localPath="G:/temp/pages/"):
    page = getHtmlBytes(baseUrl)
    urlSet = set(getInnerUrls(page,urlPatern))
    getImgInUrls(urlSet,localPath)

#https://pic1.zhimg.com/b3f2beb8f07c853195abfe7d74cf3f94_b.jpg
#https://pic3.zhimg.com/b0c91f005f6b0fccc8c1b8bdab1567aa_s.png
getImgsFromUrl("http://tieba.baidu.com/p/1091452154?see_lz=1",r'http://.{0,100}.jpg')

#getImgsFromUrl("http://tieba.baidu.com/p/3896313909",r'http://imgsrc.{0,200}.jpg')
