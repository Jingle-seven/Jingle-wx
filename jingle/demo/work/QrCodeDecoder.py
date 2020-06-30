# coding: utf-8
# 遍历解析二维码图片

import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance

dir = 'C:/Users/Administrator/Desktop/图片/二维码/'
imgPath = "示例图片.jpg"
img = Image.open(dir + imgPath)
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