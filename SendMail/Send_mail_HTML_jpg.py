#coding:utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import SendMail.Send_mail_base

class Send_mail_text_HTML_jpg(SendMail.Send_mail_base.Sendmail_Base):
    def __init__(self,user,password,sever,port,recvlist):
        SendMail.Send_mail_base.Sendmail_Base.__init__(self,user,password,sever,port,recvlist)
    def  sendmail(self,title,content,imagelistpath):
        message =  MIMEMultipart('related')
        message['From'] = self.user # 谁发的
        message['To'] = self.recvlist[0]  # 接收
        subject =title
        message['Subject'] = Header(subject, 'utf-8')
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))


        imageid=0
        for  imagepath  in imagelistpath:
            # 指定图片为当前目录
            print imagepath
            fp = open( imagepath, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            # 定义图片 ID，在 HTML 文本中引用
            imageid+=1
            msgImage.add_header('Content-ID', "<image"+str(imageid)+">")
            message.attach(msgImage)



        self.mailsever.sendmail(self.user,self.recvlist,   message.as_string())


mymail=Send_mail_text_HTML_jpg("Zy_zyong@163.com","lovechen521","smtp.163.com",25,["Zy_zyong@163.com"])
mymail.login()
mymail.sendmail("go go  go泰国",
                """
                <p>Python 邮件发送测试...</p>
                <p><img src="cid:image1"></p>
                <p><img src="cid:image2"></p>
                """
                ,
                [ r"C:\Users\Administrator\Desktop\xinjianwenjian\code\Control\1.jpg"])




