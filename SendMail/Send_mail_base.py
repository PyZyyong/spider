#coding:utf-8
import smtplib
class  Sendmail_Base:
    def __init__(self,user,password,sever,port,recvlist):
        self.user=user
        self.password=password
        self.sever=sever
        self.port=port
        self.recvlist=recvlist
    def  login(self):
        try:
            self.mailsever = smtplib.SMTP()  # 服务器端口
            self.mailsever.connect(self.sever, self.port)
            self.mailsever.login(self.user, self.password)  # 登陆
            return True
        except:
            return False

    def sendmail(self,**kwargs):
        pass
    def __del__(self):
        self.mailsever.close()
