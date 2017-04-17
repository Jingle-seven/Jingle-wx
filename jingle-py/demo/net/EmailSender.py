import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 口令(网易授权码,与网易登录密码不同)
# 不知道为什么第一个账户发送不报错, 事后却收不到邮件
acount1={"host":"smtp.163.com","user":"xiong_jin_hua@163.com","passwd":"jrqs1994"}
acount2={"host":"smtp.163.com","user":"13631435802@163.com","passwd":"xz1994"}

def sendEmail(subj="Subject",content="Blank",to="xiong_jinhua@foxmail.com",acount=acount2):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "荆人七十"
    message['To'] = to
    message['Subject'] = Header(subj, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(acount["host"], 25)  # 25 为 SMTP 端口号
        smtpObj.login(acount["user"], acount["passwd"])
        smtpObj.sendmail(acount["user"], [to, ], message.as_string())
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        raise e
    smtpObj.quit()

if __name__ =="__main__":
    sendEmail()
