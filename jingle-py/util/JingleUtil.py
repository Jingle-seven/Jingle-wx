# coding utf-8

def ipTpInt(ip):
    num = ip.split(".")
    if len(num) != 4:
        return -1
    res = int(num[0]) << 8 << 8 << 8
    res += int(num[1]) << 8 << 8
    res += int(num[2]) << 8
    res += int(num[3])

    return res


def intToIp(ipNum):
    for i in range(4):
        if i==0:
            s = str(ipNum % 256)
        else:
            s = str(ipNum % 256) + "."+s
        ipNum = ipNum // 256

    return s

if __name__ == "__main__":
    intToIp(ipTpInt("127.82.8.2"))
