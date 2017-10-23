#coding:utf-8
import time
import Control.urlcode
#整合调用
import gevent
import gevent.monkey
import GetPageData.regex.GetDataFromPage_re  #引用提取类型，正则
import GetpageSource.selenium.GetPageSourceChrome #浏览器抓取类型
import GetpageSource.selenium.GetPageSourceFireFox
import GetPageData.regex.GetDataFunc_re #选择51job,zhaopin
import GetpageSource.urllib2Go.GetPageSourceURLLIB #urllib2
import Worktype.geventcollect.gevent_task

import DataView.Data_View_bar

import SendMail.Send_mail_HTML_jpg
import threading

class  Task(threading.Thread):
    def  __init__(self,seconds,wordlist,wordlist1,emaillist):
        threading.Thread.__init__(self)
        self.seconds=seconds
        self.wordlist=wordlist  #初始化
        self.emailist=emaillist
        self.wordlist1=wordlist1

    def  run(self):  #开启线程
        while True:
            #定时操作

            urllist = []
            for word in self.wordlist:
                url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=" + Control.urlcode.Geturlcode.geturlcode(
                    word) + "&p=1&isadv=0"
                print url
                urllist.append(url)
            datalist = []

            # 选择进程或者线程抓取数据，指定抓取的类型
            gevent.monkey.patch_all()  # 自动抓取任务，自动分配
            mygevent_task = Worktype.geventcollect.gevent_task.Gevent_task()  # 初始化,对象
            # mygevent_task.run()
            go_task = [gevent.spawn(mygevent_task.run,
                                    GetpageSource.urllib2Go.GetPageSourceURLLIB.GetPageSourceURLLIB,
                                    url,
                                    GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re,
                                    GetPageData.regex.GetDataFunc_re.get_zhaopin, datalist) for url in urllist]
            gevent.joinall(go_task)  # 自动切换。开始执行
            print datalist, self.wordlist

            # 绘制图表
            mybar = DataView.Data_View_bar.DataView_bar(datalist, self.wordlist1)
            mybar.draw()
            mybar.save("1.jpg")

            mymail = SendMail.Send_mail_HTML_jpg.Send_mail_text_HTML_jpg("Zy_zyong@163.com", "lovechen521", "smtp.163.com", 25,
                                             ["Zy_zyong@163.com", "18310556724@163.com"])
            mymail.login()
            mymail.sendmail("python 职位",
                            """
                            <p>Python 邮件发送测试...</p>
                            <p><img src="cid:image1"></p>
                            """,
                            ["1.jpg"]
                            )


            print "first OK"
            time.sleep(self.seconds)

'''
if  __name__=="__main__":
    wordlist = ["python", "python 数据", "python 运维", "python 测试", "python 后端", "python web"]
    wordlist1 = [u"python", u"python 数据", u"python 运维", u"python 测试", u"python 后端", u"python web"]
    Emaillist = ["yincheng8848@163.com", "18857566375@163.com"]
    mytask=Task(120,wordlist,wordlist1,Emaillist )
    mytask.start()
    mytask.join()
    print "OK"
'''