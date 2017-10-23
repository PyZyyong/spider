#coding:utf-8
import  selenium
import selenium.webdriver  #调用浏览器，浏览器驱动放在python目录
import GetpageSource.selenium.GetPageSource #调用基类

class  GetPageSourceFireFox(GetpageSource.selenium.GetPageSource.GetPageSource):
    def  __init__(self,url):
        #父类初始化
        GetpageSource.selenium.GetPageSource.GetPageSource.__init__(self,url)
    def  getsource(self):
        driver = selenium.webdriver.Firefox()  # 调用火狐狸
        driver.get(self.url)  # 访问url
        page = driver.page_source  # 抓取网页源代码
        driver.close()
        return page

'''
testfirefox= GetPageSourceFireFox("http://www.baidu.com")
print testfirefox.getsource()
'''
