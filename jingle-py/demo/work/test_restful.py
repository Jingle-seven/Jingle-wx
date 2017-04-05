# coding: utf-8
# author: huym

import urllib.request as urllib2
import urllib
import json
import requests

# log_filePath = 'D:/test/'
log_fileName = 'test.log'

CLODINS_HOST_URL = 'localhost:9411'
HEADERS_GET = {'accept': 'application/xml'}
HEADERS_POST = {"Content-type": "application/json", "Accept": "application/json"}
HEADERS_LOG = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
USER_DATA={"username": "Tony", "password": "Tony"}
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

def postUrllib():
    url = 'http://%s/api/v1/spans' % CLODINS_HOST_URL
    fileHandle = open(log_fileName, 'r')
    fileList = fileHandle.readlines()
    for fileLine in fileList:
        line_json = json.loads(fileLine)
        params = json.dumps(line_json).encode("utf-8")

        # req = urllib2.Request(url, params, HEADERS_POST)
        req = urllib2.Request(url, params)
        response = urllib2.urlopen(req)
        print(response.read().decode("utf-8"))


def loginUrllib():
    logUrl = 'http://%s/login_process' % CLODINS_HOST_URL
    print(USER_DATA)
    userData = urllib.parse.urlencode(USER_DATA).encode('utf-8')
    req = urllib2.Request(logUrl, userData, HEADERS_LOG)
    # print(urllib2.urlopen(req).read().decode("utf-8"))
    resp = urllib2.urlopen(req)
    print(resp.read().decode("utf-8"))


def loginRequests():
    logUrl = 'http://%s/login_process' % CLODINS_HOST_URL
    s = requests.session()
    s.headers.update(HEADERS)
    resp = s.post(logUrl, USER_DATA)
    print(resp.status_code)
    print(resp.text)
    print(resp.headers)
    return s


def postSpan(ssn):
    fileHandle = open(log_fileName, 'r')
    fileList = fileHandle.readlines()

    for fileLine in fileList:
        lineJson = json.loads(fileLine)
        # params = json.dumps(line_json).encode("utf-8")
        r = ssn.post('http://%s/api/v1/spans' % CLODINS_HOST_URL,json.dumps(lineJson))
        print(r.text)

if __name__ == "__main__":
    # postUrllib()
    postSpan(loginRequests())
    print("end")