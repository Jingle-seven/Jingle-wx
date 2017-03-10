
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

fp = open(path, 'rb')
for f in fp.readlines():
    try:
        print(f.decode("unicode"))
    except Exception as e:
        continue