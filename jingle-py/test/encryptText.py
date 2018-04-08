# 加密文本，要求可逆
# 初步思路为计算unicode码。
# 将密码的几个unicode字符相与算出一个unicode密码，再将原有文本字符逐个与unicode密码进行计算
# 不过存在有些字符加密后无法用utf-8保存的问题，对于这些字符直接跳过


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
        try:
            chr(unic1).encode("utf-8")
        except Exception as e:
            errChars.add(i)
            # 如果加密后无法用utf-8保存，保留原字符
            unic1 = unic
        ciphertext.append(chr(unic1))
    print("error chars",errChars)
    return "".join(ciphertext)

fileName = "挪威的森林简析-enc-enc"
text = open('../resource/jieba/%s.txt'%fileName,encoding='utf8').read()
file = open('../resource/jieba/%s-enc.txt'%fileName, "w", encoding="utf-8")
pwd = input("input password:")
uniPwd = genPwd(pwd)
secretText = encryptText(text,uniPwd)
file.write(secretText)
print("encrypt finished")