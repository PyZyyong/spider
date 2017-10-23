#coding:utf-8
import os
import socket
import time
import threading
import Worktype.moremachine_center.web.ostools
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
client.bind((Worktype.moremachine_center.web.ostools.ostools.getip(),8848)) #绑定自身IP的8848

def  goclient():
    print "client  running"
    print os.popen("C:\Python27\python.exe C:/Users/Tsinghua-yincheng/Desktop/yinchengDaya11_last/code/Worktype/moremachine_center/Client_control.py").read()


while True:
    data,addr=client.recvfrom(4096) #接收消息
    print data  #打印消息
    threading.Thread(target=goclient).start() #开启客户端的分布式
    client.sendto("run",addr) #返回服务器执行消息
client.close()