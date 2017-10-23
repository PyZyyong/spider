#coding:utf-8
import multiprocessing #多进程
import multiprocessing.managers  #多进程管理者，跨机器
import random,time,Queue  #队列，时间，随机数

import GetPageData.regex.GetDataFromPage_re
import GetpageSource.selenium.GetPageSourceChrome
import GetPageData.regex.GetDataFunc_re

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理,共享数据
    pass

if __name__=="__main__":
    QueueManger.register("get_task")
    QueueManger.register("get_result")#注册，抓取结果，任务
    SeverIP="10.0.123.119"
    Port=8848
    manager=QueueManger(address=(SeverIP,Port),authkey=b"123456")
    manager.connect()#链接

    task=manager.get_task()
    result=manager.get_result()
    for  i  in range(5):
        try:
            t=task.get(timeout=50)#从任务中抓取
            print("取出数据",t)


            mypage = GetpageSource.selenium.GetPageSourceChrome.GetPageSourceChrome(t)
            mydata = mypage.getsource()
            myget = GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re(mydata,
                                                                            GetPageData.regex.GetDataFunc_re.get_zhaopin)  # 第一个数据，第二个函数
            num= myget.getnumbers()
            print num

            result.put(num)#数据加工后的结果
        except:
            print("队伍为空或者其他异常")
