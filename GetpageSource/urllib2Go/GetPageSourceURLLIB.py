#coding:utf-8
import GetpageSource.urllib2Go.GetPageSource
import urllib2

class  GetPageSourceURLLIB(GetpageSource.urllib2Go.GetPageSource.GetPageSource):
    def __init__(self,url):
        GetpageSource.urllib2Go.GetPageSource.GetPageSource.__init__(self,url)
    def  getsource(self):
        header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
        request = urllib2.Request(self.url, headers=header)  # 请求，修改，模拟http.
        data = urllib2.urlopen(request).read()  # 打开请求，抓取数据
        return data


'''
testfirefox= GetPageSourceURLLIB("http://www.baidu.com")
print testfirefox.getsource()
'''

