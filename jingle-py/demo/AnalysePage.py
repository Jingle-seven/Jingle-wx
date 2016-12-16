#coding=utf-8

from urllib import request
from html.parser import HTMLParser
import re

'''
HTMLParser的成员函数: 
 
    handle_startendtag  处理开始标签和结束标签 
    handle_starttag     处理开始标签，比如<xx> 
    handle_endtag       处理结束标签，比如</xx> 
    handle_charref      处理特殊字符串，就是以&#开头的，一般是内码表示的字符 
    handle_entityref    处理一些特殊字符，以&开头的，比如   
    handle_data         处理数据，就是<xx>data</xx>中间的那些数据 
    handle_comment      处理注释 
    handle_decl         处理<!开头的，比如<!DOCTYPE html PUBLIC “-//W3C//DTD HTML 4.01 Transitional//EN” 
    handle_pi           处理形如<?instruction>的东西 
 
'''

class Analyser(HTMLParser):
    def __init__(self):
         HTMLParser.__init__(self)
#         self.tag = ""
#         self.rawdata = ""
    
    def feedUrl(self,url):
        webData = request.urlopen(url).read()
        self.feed(webData.decode("utf-8"))

    def handle_starttag(self,tag, attrs):
#         print(attrs)
#         print(tag)
#         if tag=="a":
#             for (variable, value) in attrs:
#                 print(variable+": "+value)
        pass
    def handle_startendtag(self,tag, attrs):
        
        pass
    def handle_endtag(self,tag):
        
        pass
    def handle_data(self,data):
        print(data)
        pass
me = Analyser()
me.feedUrl("http://www.douban.com")
me.close()