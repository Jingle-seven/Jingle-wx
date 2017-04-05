import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"
mail_user="13631435802@163.com"
mail_pass="xz1994"   # 口令(网易授权码,与网易登录密码不同)


def sendEmail(subj="Subject",content="Blank",to="xiong_jinhua@foxmail.com",):
    sender = '13631435802@163.com'
    receivers = [to]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "荆人七十"
    message['To'] = to
    subject = subj
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        raise e

if __name__ =="__main__":
    sendEmail()
