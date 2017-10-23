#coding:utf-8
import Worktype.moremachine_abstract.Client_task
import GetPageData.regex.GetDataFromPage_re  #引用提取类型，正则
import GetpageSource.selenium.GetPageSourceChrome #浏览器抓取类型
import GetpageSource.urllib2Go.GetPageSourceURLLIB #urllib2
import GetpageSource.selenium.GetPageSourceFireFox
import GetPageData.regex.GetDataFunc_re #选择51job,zhaopin

if __name__=="__main__":
    Myclient=Worktype.moremachine_abstract.Client_task.MyClient("10.0.123.119",
                                                                8848,
                                                                b"123456",
                                                                5,
                                                                GetpageSource.urllib2Go.GetPageSourceURLLIB.GetPageSourceURLLIB,
                                                                GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re,
                                                                GetPageData.regex.GetDataFunc_re.get_zhaopin)
    Myclient.runclient()