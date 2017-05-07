# coding: utf-8
# author: xz

import re, time, random
import requests

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Referer': 'https://www.douban.com/',
           'Host': 'www.douban.com',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}


def loginDouban(user,pwd):
    print("开始登录")
    loginUrl = 'https://accounts.douban.com/login'
    formData = {
        "source": "index_nav",
        "form_email": user,
        "form_password": pwd,
        "login": u'登录',
        "remember": "on"
    }
    s = requests.session()
    s.headers.update(HEADERS)
    loginPage = s.get(loginUrl)
    formData = dict(formData, **captchaDict(loginPage.text))
    print(formData)

    # 登录
    loginResult = s.post(loginUrl, formData)
    token = re.findall(r"我的豆瓣", loginResult.text)
    if (len(token) > 0):
        print(re.findall(r"<span>.{1,20}的帐号</span>", loginResult.text),end="登录成功")
        return s
    print("登录失败")
    return False


# 获取验证码dict
def captchaDict(pageText):
    captchaIdPattern = r'<input type="hidden" name="captcha-id" value="\w{24}:en"/>'
    captchaImgPattern = r'https://www.douban.com/misc/captcha\?id=.{23,100}:en'
    captchaIdTags = re.findall(captchaIdPattern, pageText)
    if (len(captchaIdTags) == 0):
        return {}
    captchaImgUrl = re.findall(captchaImgPattern, pageText)[0]
    return {'captcha-id': captchaIdTags[0][46:73],
            'captcha-solution': inputCaptcha(captchaImgUrl, "captcha.jpg")}


# 下载验证码图片, 等待输入验证码
def inputCaptcha(captchaImgUrl, localPath, notice="please input captcha:"):
    img = requests.get(captchaImgUrl)
    size = open(localPath, 'wb').write(img.content)
    print(localPath, size, 'bytes')
    return input(notice)


def topStick(ssn, topicId, comment):
    url = "https://www.douban.com/group/topic/%s/" % topicId
    topicPage = ssn.get(url)
    ckPattern = r'name="ck" value="\w{0,10}"'
    ck = re.findall(ckPattern, topicPage.text)[0][17:-1]
    formData = {"ck": ck, "rv_comment": comment, "submit_btn": "加上去", "start": "0"}
    formData = dict(formData, **captchaDict(topicPage.text))
    print("%sadd_comment & %s" % (url, formData))
    commentResult = ssn.post(url + "add_comment#last", formData, HEADERS)
    print(re.findall('.{0,10}' + comment + '.{0,10}', commentResult.text))
    # print(commentResult.text)
    # 顶贴太多也需要输入验证码, 肝不下去了


if __name__ == "__main__":
    userPwd = ("xiong_jinhua@foxmail.com","xz121542345")
    topics = ["102257677","102179547"]
    words = "披星戴月地奔波只为一扇窗帮顶随便一挥手就是漂亮的十五字"
    #登录
    loginSuc = loginDouban(userPwd[0],userPwd[1])
    while not loginSuc:
        loginSuc = loginDouban(userPwd[0],userPwd[1])

    #顶贴
    while loginSuc:
        if 8 < time.localtime()[3] < 24:
            for i in topics:
                topStick(loginSuc, i, random.choice(words))
                time.sleep(random.randint(15, 35) * 60)
        time.sleep(random.randint(15, 35) * 60)
