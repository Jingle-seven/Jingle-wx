# 加密文本，要求可逆
# 初步思路为计算unicode码。
# 将密码的几个unicode字符相与算出一个unicode密码，再将原有文本字符逐个与unicode密码进行计算
# 不过存在有些字符加密后无法用utf-8保存的问题，待解决


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
        unic1 = unic ^ uniPwd
        ciphertext.append(chr(unic1))
        # 有些密文无法用utf-8编码，待解决
        try:
            chr(unic1).encode("utf-8")
        except Exception as e:
            print(i,unic1)
            errChars.add(i)
    print(errChars)
    return "".join(ciphertext)

fileName = "挪威的森林简析"
text = open('../resource/jieba/%s.txt'%fileName,encoding='utf8').read()
file = open('../resource/jieba/%s-enc.txt'%fileName, "w", encoding="utf-8")
pwd = "逗比"
uniPwd = genPwd(pwd)
secretText = encryptText(text,uniPwd)
# print(text)
# print(secretText)
# file.write(secretText)
print(encryptText(secretText,uniPwd))