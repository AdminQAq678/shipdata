import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#! /usr/bin/env
# python
#qq邮箱smtp服务器

host_server = 'smtp.qq.com'#sender_qq为发件人的qq号码
sender_qq = 'qaq678678@qq.com'#pwd为qq邮箱的授权码
pwd = 'dunfonuhdnacjged' ## xh**********bdc
#发件人的邮箱
sender_qq_mail = 'qaq678678@qq.com'
#收件人邮箱
receiver = '2549793997@qq.com'
#邮件的正文内容
mail_content = '<h1>请点击以下连接找回密码</h1><a>http://localhost:8787/login</a><br>' \
               '<a>www.wocnz.club</a>'
#邮件标题
mail_title = 'hello'
#ssl登录
smtp = smtplib.SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
# smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)


msg = MIMEMultipart()#多部分
msg["Subject"] = Header(mail_title, 'utf-8')#构造头部信息
msg["From"] = Header("Wocnz", 'utf-8')
msg["To"] = Header("接收人", 'utf-8')
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))#添加主题信息到msg中
att1 = MIMEText(open('head.jpg', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="attach.jpg"'
msg.attach(att1)
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()