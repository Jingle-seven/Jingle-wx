# coding: utf-8
# author: huym

import urllib
import json

log_filePath = 'D:/test/'
log_fileName = 'test.log'

cloudins_server_ip = 'localhost:9411'
CONST_headers_get = {'accept': 'application/xml'}
CONST_headers_post = {"Content-type": "application/json", "Accept": "application/json"}

def post_restful():
    url = 'http://%s/api/v1/spans' % cloudins_server_ip

    fileHandle = open(log_filePath + log_fileName, 'r')
    fileList = fileHandle.readlines()
    for fileLine in fileList:
        line_json = json.loads(fileLine)
        params = json.dumps(line_json)
        req = urllib.request.Request(url, params, CONST_headers_post)
        response = urllib.urlopen(req)
        print(response.read())

if __name__ == "__main__":
    post_restful()