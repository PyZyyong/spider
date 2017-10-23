#coding:utf-8
import GetPageData.GetDataFromPage

class  GetDataFromPage_xpath(GetPageData.GetDataFromPage.GetDataFromPage):
    def __init__(self,pagedata,func_get):
        GetPageData.GetDataFromPage.GetDataFromPage.__init__(self,pagedata,func_get)
    def getnumbers(self):
        return    self.func_get(self.pagedata)