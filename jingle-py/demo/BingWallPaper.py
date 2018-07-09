# coding=utf-8
import urllib.request as request
from PIL import Image
import win32gui,win32con
import time,json,threading,random,sys

"""
    也使用了一个开源项目提供的API,地址:https://github.com/xCss/bing
"""
BASE_DIR = "G:/temp/photo/"
API_URI = "https://bing.ioliu.cn"
BING_URI = "http://cn.bing.com"
BING_STORY = "http://cn.bing.com/cnhp/coverstory"
BING_INFO = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=%s&n=1"

def getImgInfo(idx=0):
    content = request.urlopen(BING_INFO%idx).read()
    info = content.decode("utf-8")
    infoMap = json.loads(info)["images"][0]

    describe = json.loads(request.urlopen(BING_STORY).read().decode("utf-8"))["para1"]
    print(describe)
    # for k,v in infoMap.items():
    #     print("%s: %s"%(k,v))
    return infoMap

def getImgInfoByApi(idx):
    imgInfoUrl = API_URI + "/v1?d=%d" % idx
    content = request.urlopen(imgInfoUrl).read()
    info = content.decode("utf-8")
    infoMap = json.loads(info)["data"]
    # for k,v in infoMap.items():
    #     print("%s: %s"%(k,v))

    return infoMap

def getImgByApi(idx=0):
    if idx>= 0:
        imgInfo = getImgInfoByApi(idx)
        imgUrl = imgInfo["url"]
        localImgPath = BASE_DIR + imgInfo["title"] + ".jpg"
        print(imgInfo["description"])
    elif idx == -1:
        imgUrl = API_URI + "/v1/rand"
        localImgPath = BASE_DIR + str(random.randint(100000,999999)) + ".jpg"
    else:
        print("RAW")
        imgInfo = getImgInfo()
        imgUrl = BING_URI + imgInfo["url"]
        localImgPath = BASE_DIR + imgInfo["fullstartdate"] + ".jpg"
    request.urlretrieve(imgUrl, localImgPath)
    return localImgPath

def setWallPaper(imgPath):
    bmpPath = imgPath.split(".")[0] + ".bmp"
    img = Image.open(imgPath)
    img.save(bmpPath)
    # os.remove(imgPath)
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmpPath, 0)

def paperSetter(period,index):
    while(True):
        # setWallPaper(getImgByApi(index))
        try:
            setWallPaper(getImgByApi(index))
            pass
        except Exception as e:
            print(e)
        time.sleep(period)


def runTread():
    index = 0
    period = 60 * 60 * 24
    try:
        index = int(sys.argv[1])
        period = int(sys.argv[2])
    except Exception as e:
        print(e)
    if index >= 0:
        print("%d 天前的Bing推送图片" % index)
    elif index== -1:
        print("随机一张Bing图片")
    print("%d 秒更新一次" % period)
    t1 = threading.Thread(target=paperSetter, args=(period, index))  # args逗号不能少,不然就不是元组
    t1.start()


if __name__ == '__main__':
    runTread()
    # getgetImgInfo()