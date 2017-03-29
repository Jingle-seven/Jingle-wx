# coding=utf-8
import urllib.request as request
from PIL import Image
import win32gui,win32con
import time,json,threading,random,sys

BASE_DIR = "G:/temp/photo/"
BASE_API = "https://bing.ioliu.cn/v1"

def getImgInfo(idx):
    imgInfoUrl = BASE_API + "?d=%d" % idx
    content = request.urlopen(imgInfoUrl).read()
    info = content.decode("utf-8")
    infoMap = json.loads(info)["data"]
    # for k,v in infoMap.items():
    #     print("%s: %s"%(k,v))

    return infoMap

def getImg(idx=0):
    if idx>= 0:
        imgInfo = getImgInfo(idx)
        imgUrl = imgInfo["url"]
        localImgPath = BASE_DIR + imgInfo["title"] + ".jpg"
        print(imgInfo["description"])
    else:
        imgUrl = BASE_API + "/rand"
        localImgPath = BASE_DIR + str(random.randint(100000,999999)) + ".jpg"

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
        try:
            setWallPaper(getImg(index))
            print("壁纸改完了")
        except Exception as e:
            print(e)
        time.sleep(period)

if __name__ == '__main__':
    index = 0
    period = 60 *60 *24
    try:
        index = int(sys.argv[1])
        period = int(sys.argv[2])
    except Exception as e:
        print(e)
    if index >=0:
        print("%d天前的Bing推送图片"%index)
    else:
        print("随机一张Bing图片")
    print("%d秒更新一次"%period)

    t1 = threading.Thread(target=paperSetter, args=(period,index))# args逗号不能少,不然就不是元组
    t1.start()