from urllib import request
import re,urllib2,json,sys

def getHtmlBytes(url):
    webData = request.urlopen(url).read()
    #print(webData)
    return webData

#一楼
if __name__ == "__main__":
    cj = cookielib.CookieJar()
    body = (('nickname','用户名'), ('password','密码'))
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
    urllib2.install_opener(opener)
 
    url = 'http://login.hi.mop.com/Login.do'
    req=urllib2.Request(url,urllib.urlencode(body))
    u=urllib2.urlopen(req)
    login=u.read().decode('utf-8').encode('gbk')
    print re.findall('\<title\>(.+)\<',login)[0]
     
    #打卡领MP
    mpurl='http://home.hi.mop.com/ajaxGetContinusLoginAward.do'
    mp=opener.open(urllib2.Request(mpurl)).read()
    if mp=='5':
        print '打卡成功 MP+5'

#二楼
def request_ajax_data(url,data,referer=None,**headers):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116')
    if referer:
        req.add_header('Referer',referer)
    if headers:
        for k in headers.keys():
            req.add_header(k,headers[k])

    params = urllib.urlencode(data)
    response = urllib2.urlopen(req, params)
    jsonText = response.read()
    return json.loads(jsonText)

ajaxRequestBody = {"blogId":blogId,"postId":entryId,"blogApp":blogApp,"blogUserGuid":blogUserId}
ajaxResponse = request_ajax_url('http://outofmemory.cn/fakeAjax',ajaxRequestBody)