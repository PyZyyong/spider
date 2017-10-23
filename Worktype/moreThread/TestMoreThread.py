#coding:utf-8
import Worktype.moreThread.BaseThread  #引用多线程的线程模块
import GetPageData.regex.GetDataFromPage_re  #引用提取类型，正则
import GetpageSource.selenium.GetPageSourceChrome #浏览器抓取类型
import GetpageSource.urllib2Go.GetPageSourceURLLIB #urllib2
import GetpageSource.selenium.GetPageSourceFireFox
import GetPageData.regex.GetDataFunc_re #选择51job,zhaopin


urllist=["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%95%B0%E6%8D%AE&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%B5%8B%E8%AF%95&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20web&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E8%BF%90%E7%BB%B4&p=1&isadv=0"]

threadlist=[]
for  url  in urllist:
    mythd=Worktype.moreThread.BaseThread.BaseThread(GetpageSource.urllib2Go.GetPageSourceURLLIB.GetPageSourceURLLIB,
                                                    url,
                                                    GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re,
                                                    GetPageData.regex.GetDataFunc_re.get_zhaopin)
    mythd.start()
    threadlist.append(mythd)
for  thd in threadlist:
    thd.join()
print "over"

