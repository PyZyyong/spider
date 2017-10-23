#coding:utf-8
import os
class  ostools:
    @staticmethod  #静态方法
    def  getip():
        file=  os.popen("ipconfig")
        while  True:
            line=file.readline()
            if not line:
                break
            ipstr=None
            if  line.find("IPv4")!=-1:
                linelist=line.split(":")
                ipstr= linelist[1].strip()
                print ipstr
                break

        return ipstr
#ostools.getip()