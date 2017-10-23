#coding:utf-8
import threading

class  BaseThread(threading.Thread):
    def __init__(self,GetpageSourcetype,url,Getdatatype,Getfunc,queue):
        threading.Thread.__init__(self)
        #抓取网页的类型，链接，正则或者xpath,函数51job,zhaopin
        self.GetpageSourcetype=GetpageSourcetype
        self.url=url
        self.Getdatatype=Getdatatype
        self.Getfunc=Getfunc
        self.queue=queue #队列，收集结果

    def run(self):
        #GetpageSourcetype抓取网页的类型，chrome,firefox
        #Getdatatype,re,bs4,xpath
        #Getfunc  调用函数
        #url  链接
        mypage =  self.GetpageSourcetype( self.url)
        mydata = mypage.getsource()
        myget=   self.Getdatatype( mydata, self.Getfunc)
        print myget.getnumbers(),self.getName()
        self.queue.put([myget.getnumbers(),self.url]) #压入数据
