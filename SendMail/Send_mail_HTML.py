#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import SendMail.Send_mail_base

class Send_mail_text_HTML(SendMail.Send_mail_base.Sendmail_Base):
    def __init__(self,user,password,sever,port,recvlist):
        SendMail.Send_mail_base.Sendmail_Base.__init__(self,user,password,sever,port,recvlist)
    def  sendmail(self,title,content,fromname,recvname):
        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = self.user # 谁发的
        message['To'] = self.recvlist[0]  # 接收
        subject =title
        message['Subject'] = Header(subject, 'utf-8')
        self.mailsever.sendmail(self.user,self.recvlist,   message.as_string())
'''
mymail=Send_mail_text_HTML("yincheng8848@163.com","tsinghua8848","smtp.163.com",25,["yincheng8848@163.com","18310556724@163.com"])
mymail.login()
mymail.sendmail("go go  go泰国","  <p><a href=\"http://www.baidu.com\">这是一个链接</a></p> ","yincheng","sunqing")


'''