#coding:utf-8
class  Process_task:
    def run(self,GetpageSourcetype,url,Getdatatype,Getfunc,queue):
        #GetpageSourcetype抓取网页的类型，chrome,firefox
        #Getdatatype,re,bs4,xpath
        #Getfunc  调用函数
        #url  链接
        mypage = GetpageSourcetype(url)
        mydata = mypage.getsource()
        myget=  Getdatatype( mydata,Getfunc)
        print myget.getnumbers()
        queue.put([myget.getnumbers(),url])#压入共享队列
