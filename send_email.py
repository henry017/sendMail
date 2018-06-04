#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# 解决邮件中文乱码问题
# 增加发送附件功能

import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def getnow():
    return time.strftime('%F %T', time.localtime())

'''
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
'''

def sendMail(content):
    # 企业邮箱服务smtp地址端口信息
    smtp_server = 'smtp.mxhichina.com'  #smtp服务地址
    from_mail = 'your email'   #邮箱账号
    mail_passwd = 'your password'  #密码 有的邮箱比如qq|163需要填的是客户端授权码
    to_mail = ['email1@qq.com', 'email2@qq.com']  #发送目标
    subject = '任务' + getnow()

    msg = MIMEMultipart()
    msg['From'] = Header('兰子君 <%s>' % from_mail, 'utf-8')
    # ;号连接 让客户端单个显示邮箱
    msg['To'] = Header('%s' % ';'.join(i for i in to_mail))
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    # attach
    att = MIMEText(open('C:\Doc\Iptables\iptables.txt', 'rb').read(), 'base64', 'utf-8')
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="iptables.txt"'
    msg.attach(att)
    
    # picture
    with open(r'C:\Users\Kongs\Pictures\google_ac.png', 'rb') as p:
        msgimage = MIMEImage(p.read())
    msgimage.add_header('Content-Disposition', 'attachment', filename='google_ac.png')
    msgimage.add_header('Content-ID', '<O>')
    msgimage.add_header('X-Attachment-Id', 'O')
    msg.attach(msgimage)

    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, 25)
        #s.set_debuglevel(1)
        s.login(from_mail, mail_passwd)
        s.sendmail(from_mail, to_mail, msg.as_string())
        s.quit()
        print("%s 邮件发送成功!" % getnow())
    except smtplib.SMTPException as e:
        print("%s 邮件发送失败! Error_info: %s" % (getnow(), e))

if __name__ == '__main__':
    content = getnow() + '''
本篇教程中将带您完成下列任务

1.创建一个Scrapy项目
2.定义提取的Item
3.编写爬取网站的 spider 并提取 Item
4.编写 Item Pipeline 来存储提取到的Item(即数据)
'''
    sendMail(content)
