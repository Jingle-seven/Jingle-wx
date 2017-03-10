# encoding=utf8
import os
import struct

def getLast128K(path, file):
    ff1 = open(os.path.join(path, file), "rb")
    ff1.seek(-128, 2)
    id3v1data = ff1.read()
    ff1.close()
    return id3v1data


def getAllBinData(path, file):
    ff1 = open(os.path.join(path, file), "rb")
    data = ff1.read()
    ff1.close()
    return data


def setTag(path, file, title="".encode("utf-8"), artist="".encode("utf-8"), album="".encode("utf-8"),
           year="".encode("utf-8"), comment="".encode("utf-8"), genre="".encode("utf-8")):
    """
    设置mp3的ID3 v1中的部分参数
    char Header[3]; /*标签头必须是"TAG"否则认为没有标签*/
    char Title[30]; /*标题*/
    char Artist[30]; /*作者*/
    char Album[30]; /*专集*/
    char Year[4]; /*出品年代*/
    char Comment[30]; /*备注*/
    char Genre; /*类型*/
    mp3文件尾部128字节为id3v1的数据，如果有数据则读取修改，无数据则补充
    """

    header = 'TAG'.encode("utf-8")
    str = struct.pack('3s30s30s30s4s30ss', header, title, artist, album, year, comment, genre)
    data = getAllBinData(path, file)
    infoData = getLast128K(path, file)
    # ff = open(os.path.join(path, file), "wb")
    print(infoData.decode("gb2312"))
    # print(data.decode("gb2312"))
    try:
        if infoData[0:3] != header:# 判断是否有id3v1数据if id3v1data[0:3]!=header:#倒数128字节不是以TAG开头的说明没有#按照id3v1的结构补充上去
            # ff.write(data + str)
            pass
        else:
            # ff.write(data[0:-128] + str)
            pass
        # ff.close()
        print("OK " + file)
    except Exception as e:
        # ff.write(data)
        print("Error " + title.decode("gbk"))

if __name__ == "__main__":  # 我存放mp3文件的目录
    path = "F:\\audio\\新建文件夹\\"
    file = "李健 - 传奇 - 副本.mp3"
    artist = "梁静茹".encode('utf-8')
    setTag(path,file)
