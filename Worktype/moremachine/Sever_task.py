#coding:utf-8
import multiprocessing #多进程
import multiprocessing.managers  #多进程管理者，跨机器
import random,time,Queue  #队列，时间，随机数

task_queue=Queue.Queue() #任务队列
result_queue=Queue.Queue() #结果队列初始化

def return_task():  #返回任务队列
    return task_queue

def  return_result(): #返回结果队列
    return result_queue

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理,共享数据
    pass

if __name__=="__main__":
    multiprocessing.freeze_support() #开启分布式支持
    #注册共享 #其他进程可以按照get_task调用return_task
    QueueManger.register("get_task",callable=return_task)
    QueueManger.register("get_result", callable=return_result)
    manger=QueueManger(address=("10.0.123.119",8848),authkey=b"123456")#管理者的IP，密码
    manger.start()#开启
    task,result=manger.get_task(),manger.get_result()#task,任务，resulit结果

    urllist = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%95%B0%E6%8D%AE&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%B5%8B%E8%AF%95&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20web&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E8%BF%90%E7%BB%B4&p=1&isadv=0"]

    for  url  in urllist :
        print("task加入数据",url)
        task.put(url) #压入结果

    print("开始等待结果")

    for  i in range(len(urllist)):
        myresult=result.get(timeout=50)
        print("抓取到数据",myresult)
    manger.shutdown()#关闭服务器


