#coding:utf-8
import urllib2

import GetpageSource.MyAgent
import GetpageSource.urllib2Go.GetPageSource
import random

class  GetPageSourceURLLIBByname(GetpageSource.urllib2Go.GetPageSource.GetPageSource):
    def __init__(self,url):
        GetpageSource.urllib2Go.GetPageSource.GetPageSource.__init__(self,url)
    def  getsource(self,name):
        myagent = GetpageSource.MyAgent.Myagent()  # 创建一个代理对象
        try:
            agentstr= myagent.pcUserAgent[name]
        except:
            return None
        print agentstr
        randomlist=agentstr.split(":")
        header = {randomlist[0]: randomlist[1]}

        request = urllib2.Request(self.url, headers=header)  # 请求，修改，模拟http.
        data = urllib2.urlopen(request).read()  # 打开请求，抓取数据
        return data
'''
testfirefox= GetPageSourceURLLIBByname("http://www.baidu.com")
print testfirefox.getsource("IE 8.0")
'''
