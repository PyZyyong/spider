#coding:utf-8
import gevent
import gevent.monkey
import GetPageData.regex.GetDataFromPage_re  #引用提取类型，正则
import GetpageSource.selenium.GetPageSourceChrome #浏览器抓取类型
import GetpageSource.selenium.GetPageSourceFireFox
import GetPageData.regex.GetDataFunc_re #选择51job,zhaopin
import GetpageSource.urllib2Go.GetPageSourceURLLIB #urllib2
import Worktype.geventcollect.gevent_task

datalist=[]
urllist=["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%95%B0%E6%8D%AE&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%B5%8B%E8%AF%95&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20web&p=1&isadv=0",
         "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E8%BF%90%E7%BB%B4&p=1&isadv=0"]
gevent.monkey.patch_all()#自动抓取任务，自动分配
mygevent_task=Worktype.geventcollect.gevent_task.Gevent_task()#初始化,对象
#mygevent_task.run()
go_task=[ gevent.spawn(mygevent_task.run,
                       GetpageSource.urllib2Go.GetPageSourceURLLIB.GetPageSourceURLLIB,
                       url,
                       GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re,
                       GetPageData.regex.GetDataFunc_re.get_zhaopin,datalist)          for url  in urllist    ]
gevent.joinall(go_task) #自动切换。开始执行
print datalist
