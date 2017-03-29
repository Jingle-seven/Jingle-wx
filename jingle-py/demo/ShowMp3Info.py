import sys

def getID3(filename):
    fp = open(filename, 'rb')
    fp.seek(-128, 2)

    fp.read(3)  # TAG iniziale
    title = fp.read(30)
    artist = fp.read(30)
    album = fp.read(30)
    anno = fp.read(4)
    comment = fp.read(28)
    fp.close()

    return {'title': title, 'artist': artist, 'album': album, 'anno': anno}

path = "F:\\audio\\新建文件夹\\李健 - 传奇 - 副本.mp3"
print(getID3(path))

print(sys.getdefaultencoding())
# fp = open(path, 'rb')
# for f in fp.readlines():
#     try:
#         print(f.decode("unicode"))
#     except Exception as e:
#         continue

# encoding: utf8
import sys
import os
import binascii
import json


def get_id3data(fp):
    id3_data = {}
    frame_id = ['TIT2', 'TYER', 'TRCK', 'TALB', 'TPE2', 'COMM', 'TPE1']

    fp.read(10)

    while True:
        fid = fp.read(4)
        if fid not in frame_id:
            break
        size = int(binascii.b2a_hex(fp.read(4)), 16)
        fp.read(2)
        id3_data[fid] = fp.read(size).strip('\x00')
    return id3_data


if __name__ == '__main__':
    abspath = os.path.abspath(path)
    path, filename = os.path.split(abspath)

    fp = open(os.path.join(path, filename), 'rb')
    id3_data = get_id3data(fp)
    print(id3_data)
    # print(json.dumps(id3_data, ensure_ascii=False, encoding='gbk'))
    fp.close()