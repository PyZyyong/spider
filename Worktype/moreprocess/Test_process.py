#coding:utf-8
import  multiprocessing
import Worktype.moreprocess.Process_task
import GetPageData.regex.GetDataFromPage_re  #引用提取类型，正则
import GetpageSource.selenium.GetPageSourceChrome #浏览器抓取类型
import GetpageSource.selenium.GetPageSourceFireFox
import GetPageData.regex.GetDataFunc_re #选择51job,zhaopin
import GetpageSource.urllib2Go.GetPageSourceURLLIB #urllib2

if __name__ =="__main__":
    queue=multiprocessing.Queue()#进程之间共享数据
    urllist=["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
             "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%95%B0%E6%8D%AE&p=1&isadv=0",
             "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%B5%8B%E8%AF%95&p=1&isadv=0",
             "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20web&p=1&isadv=0",
             "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E8%BF%90%E7%BB%B4&p=1&isadv=0"]
    processlist=[]#进程列表
    p_task=Worktype.moreprocess.Process_task.Process_task()#任务对象
    for  url  in urllist:
        p=multiprocessing.Process(target= p_task.run,args=(GetpageSource.urllib2Go.GetPageSourceURLLIB.GetPageSourceURLLIB,
                                                           url,
                                                           GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re,
                                                            GetPageData.regex.GetDataFunc_re.get_zhaopin,
                                                            queue))
        p.start()
        processlist.append(p)#加入进程列表

    for  p  in  processlist:
        p.join() #等待所有进程退出
    while  not  queue.empty():
        data=queue.get()  #共享队列取出数据
        print "queue",data