#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import SendMail.Send_mail_base

class Send_mail_text(SendMail.Send_mail_base.Sendmail_Base):
    def __init__(self,user,password,sever,port,recvlist):
        SendMail.Send_mail_base.Sendmail_Base.__init__(self,user,password,sever,port,recvlist)
    def  sendmail(self,title,content):
        msg = MIMEText(content)  # 转换邮件文本,内容
        msg['Subject'] = title # 标题
        msg['From'] = self.user # 谁发的
        msg['To'] =self.recvlist[0]  # 接收
        self.mailsever.sendmail(self.user,self.recvlist,msg.as_string())



'''
mymail=Send_mail_text("yincheng8848@163.com","tsinghua8848","smtp.163.com",25,                     ["yincheng8848@163.com","18310556724@163.com"])
mymail.login()
mymail.sendmail(u"hello  sunqing",u"go go  go")

'''
