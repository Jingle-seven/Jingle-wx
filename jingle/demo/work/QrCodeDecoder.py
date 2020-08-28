# coding: utf-8
# 遍历解析二维码图片

import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance
import os

dir = 'C:/Users/Administrator/Desktop/图片/二维码/'
imgPath = "示例图片.jpg"
def decodeOnePic(path):
    img = Image.open(path)
    # img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
    # img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
    # img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
    # img = img.convert('L')#灰度化
    # img.show()
    codes = pyzbar.decode(img) #一个图片中可能有多个二维码
    # print(codes)
    for code in codes:
        barcodeData = code.data.decode("utf-8")
        print(barcodeData)

if __name__ == "__main__":
    # decodeOnePic(dir+'搜狗截图20200827095748.jpg')
    for fileName in os.listdir(dir):
        # print(fileName)
        try:
            decodeOnePic(dir + fileName)
        except Exception as e:
            print(e)