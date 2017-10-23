#coding:utf-8
import urllib2

import GetpageSource.MyAgent
import GetpageSource.urllib2Go.GetPageSource
import random

class  GetPageSourceURLLIBRandom(GetpageSource.urllib2Go.GetPageSource.GetPageSource):
    def __init__(self,url):
        GetpageSource.urllib2Go.GetPageSource.GetPageSource.__init__(self,url)
    def  getsource(self):
        myagent= GetpageSource.MyAgent.Myagent()#创建一个代理对象 ,
        myagentlist=[] #列表，保存字典内部的代理信息
        for  key in myagent.pcUserAgent: #循环字典
            myagentlist.append(myagent.pcUserAgent[key])
        randomagent= random.choice( myagentlist) #随机抓取
        #print type(randomagent)  字符串类型
        randomlist=randomagent.split(":")
        #print randomlist  代理信息

        header = {randomlist[0]: randomlist[1]}

        request = urllib2.Request(self.url, headers=header)  # 请求，修改，模拟http.
        data = urllib2.urlopen(request).read()  # 打开请求，抓取数据
        return data


'''
testfirefox= GetPageSourceURLLIBRandom("http://www.baidu.com")
print testfirefox.getsource()
'''



