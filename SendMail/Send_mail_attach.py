#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import SendMail.Send_mail_base

class Send_mail_text_attch(SendMail.Send_mail_base.Sendmail_Base):
    def __init__(self,user,password,sever,port,recvlist):
        SendMail.Send_mail_base.Sendmail_Base.__init__(self,user,password,sever,port,recvlist)
    def  sendmail(self,title,content,pathlist):
        message = MIMEMultipart()
        message['From'] = self.user # 谁发的
        message['To'] = self.recvlist[0]  # 接收
        subject =title
        message['Subject'] = Header(subject, 'utf-8')
        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        #按照路径添加附件
        for filepath  in pathlist:
            att1 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = "attachment; filename=\""+ filepath +"\""
            message.attach(att1)

        self.mailsever.sendmail(self.user,self.recvlist,   message.as_string())

'''

mymail=Send_mail_text_attch("yincheng8848@163.com","tsinghua8848","smtp.163.com",25,["yincheng8848@163.com","18310556724@163.com"])
mymail.login()
#mymail.sendmail("go go  go泰国","  <p><a href=\"http://www.baidu.com\">这是一个链接</a></p> ",["__init__.py","Send_mail_base.py"])
mymail.sendmail("go go  go泰国","  <p><a href=\"http://www.baidu.com\">这是一个链接</a></p> ",[r"C:\Users\Tsinghua-yincheng\Desktop\yinchengDaya11_down_last\Testcode\smtp\1.png",r"C:\Users\Tsinghua-yincheng\Desktop\yinchengDaya11_down_last\Testcode\smtp\2.png"])

'''


