#coding:utf-8
import urllib
class  Geturlcode:
    @staticmethod
    def geturlcode(url):
        return urllib.quote(url) #进行编码

    @staticmethod
    def geturlfromcode(code):
        return urllib.unquote(code) # 进行编码

#print Geturlcode.geturlcode("python 数据")
#print Geturlcode.geturlfromcode(Geturlcode.geturlcode("python 数据"))
