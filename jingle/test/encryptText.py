# 加密文本，要求可逆
# 初步思路为计算unicode码。
# 将密码的几个unicode字符相与算出一个unicode密码，再将原有文本字符逐个与unicode密码进行计算
# 不过存在有些字符加密后无法用utf-8保存的问题，对于这些字符直接跳过
import sys


def genPwd(rawPwd):
    uniPwd = 0b0
    for i in rawPwd:
        uniPwd ^= ord(i)
        # print(uniPwd)
    return uniPwd

def encryptText(rawText ,uniPwd):
    ciphertext = []
    errChars = set()
    for i in rawText:
        unic = ord(i)
        unicEnc = unic ^ uniPwd
        try:
            # 如果加密后无法用utf-8保存，保留原字符
            chr(unicEnc).encode("utf-8")
            if unicEnc==13:
                raise Exception("不转换为换行符,因无法妥善保存")
        except Exception as e:
            errChars.add(i)
            unicEnc = unic
        # print("%s -> %s"%(i,chr(unicEnc)))
        ciphertext.append(chr(unicEnc))
    # print("error chars",errChars)
    return "".join(ciphertext)



def encFile(fileName,pwd):
    text = open(fileName, encoding='utf8').read()
    file = open('%s.enc' % fileName, "w", encoding="utf-8")
    secretText = encryptText(text, genPwd(pwd))
    file.write(secretText)
    print("{0} was encrypted to {0}.enc".format(fileName))


def encFileCmd():
    try:
        fileName = sys.argv[1]
    except Exception as e:
        fileName = input("input file name:")
    try:
        pwd = sys.argv[2]
    except Exception as e:
        pwd = input("input password:")
    encFile(fileName, pwd)


# encFileCmd()
fileName = "weibo.sql"
pwd = input("input password:")
encFile(fileName,pwd)
encFile("%s.enc"%fileName,pwd)
