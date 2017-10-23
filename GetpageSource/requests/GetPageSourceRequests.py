#coding:utf-8
import GetpageSource.requests.GetPageSource
import requests
class GetPageSourceRequests(GetpageSource.requests.GetPageSource.GetPageSource):
    def __init__(self,url,decodetype):
        GetpageSource.requests.GetPageSource.GetPageSource.__init__(self,url)
        self.decodetype=decodetype
    def  getsource(self):
        req = requests.get(self.url, verify=True)  # 访问https
        return req.text.encode(self.decodetype)


'''
testfirefox= GetPageSourceRequests("http://www.baidu.com","utf-8")
print testfirefox.getsource()
'''

