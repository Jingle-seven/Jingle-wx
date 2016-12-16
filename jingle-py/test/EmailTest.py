import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="13631435802@163.com"    #用户名
mail_pass="xz121542345"   #口令


sender = '13631435802@163.com'
receivers = ['xiong_jinhua@foxmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('这里是内容', 'plain', 'utf-8')
# message['From'] = Header("13631435802@163.com", 'utf-8')
# message['To'] =  Header("xiong_jinhua@foxmail.com", 'utf-8')
message['From'] = "这里是发件人称呼"
message['To'] =  "xiong_jinhua@foxmail.com"

subject = '这里是主题'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    raise e
