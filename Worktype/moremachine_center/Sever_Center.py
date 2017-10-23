#coding:utf-8
import os
import socket
import threading
dest=("<broadcast>",8848)
sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#UDP
#修改网络参数，实现广播设定
sever.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

def gosever():
    print "sever  running"
    print os.popen("C:\Python27\python.exe C:/Users/Tsinghua-yincheng/Desktop/yinchengDaya11_last/code/Worktype/moremachine_center/Sever_control.py").read()


while True:
    data=raw_input("输入数据")
    #os.system("notepad")
    threading.Thread(target=gosever).start()
    sever.sendto(data,dest)
    recv=sever.recvfrom(4096)
    print recv

