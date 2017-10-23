#coding:utf-8
import multiprocessing #多进程
import multiprocessing.managers  #多进程管理者，跨机器
import random,time,Queue  #队列，时间，随机数
import GetPageData.regex.GetDataFromPage_re
import GetpageSource.selenium.GetPageSourceChrome
import GetPageData.regex.GetDataFunc_re

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理,共享数据
    pass

class  MyClient:
    def __init__(self,ip,port,password,tasknumbers,GetpageSourcetype,Getdatatype,Getfunc):
        self.ip=ip
        self.port=port
        self.password=password
        self.GetpageSourcetype=GetpageSourcetype  #IE，chrome
        self.Getdatatype=Getdatatype  #re,bs4, xpath
        self.Getfunc=Getfunc  #51job,zhaopin
        self.tasknumbers=tasknumbers #任务数量
    def runclient(self):
        QueueManger.register("get_task")
        QueueManger.register("get_result")  # 注册，抓取结果，任务
        manager = QueueManger(address=(self.ip, self.port), authkey=self.password)
        manager.connect()  # 链接
        task = manager.get_task()
        result = manager.get_result()

        for i in range(self.tasknumbers):
            #try:
                url = task.get(timeout=50)  # 从任务中抓取
                print("取出url", url)
                num=0
                mypage = self.GetpageSourcetype(url)#创建对象，
                mydata = mypage.getsource() #提取网页源代码
                myget = self.Getdatatype(mydata, self.Getfunc)#提取方式，
                num=myget.getnumbers() #抓取数据

                print num
                result.put(num)  # 数据加工后的结果
            #except:
                #print("队伍为空或者其他异常")
