#coding=utf-8
import urllib.request  
import http.cookiejar  
import re

def getHtmlBytes(url):
    webData = request.urlopen(url).read()
    #print(webData)
    return webData

# http://www.tuicool.com/comments.json?aid=2qqmuaf&html_body=内容&auth=OTgxMjE
#header{X-CSRF-Token:IH3TIkSy9QKm+pZEJVgox8dVsL20YAt2N0YdbjlnsU8=,Cookie:_tuicool_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFRkkiJTllM2YyN2UzYWQ5ZWUzODQyNmIzZjA4NDI5ODA2OWIzBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUlIM1RJa1N5OVFLbStwWkVKVmdveDhkVnNMMjBZQXQyTjBZZGJqbG5zVTg9BjsARkkiDHVzZXJfaWQGOwBGaQNJfwFJIg5yZXR1cm5fdG8GOwBGSSIsaHR0cDovL3d3dy50dWljb29sLmNvbS9hcnRpY2xlcy8ycXFtdWFmBjsARg%3D%3D--5f27c508098bbf614546868fdbe1b374a33b0d35}