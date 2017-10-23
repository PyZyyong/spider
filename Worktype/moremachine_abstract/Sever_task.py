#coding:utf-8
import multiprocessing #多进程
import multiprocessing.managers  #多进程管理者，跨机器
import random,time,Queue  #队列，时间，随机数

class  QueueManger(multiprocessing.managers.BaseManager):#继承，进程管理,共享数据
    pass

class   MainSever:
    task_queue = Queue.Queue()  # 任务队列
    result_queue = Queue.Queue()  # 结果队列初始化
    def  __init__(self,ip,port,tasklist,password):

        self.ip=ip
        self.port=port
        self.tasklist=tasklist  # ip。端口，任务列表
        self.authkey=password #

    def return_task(self):  # 返回任务队列
        return self.task_queue

    def return_result(self):  # 返回结果队列
        return self.result_queue

    def runsever(self):

        QueueManger.register("get_task", callable=self.return_task)
        QueueManger.register("get_result", callable=self.return_result)
        manger = QueueManger(address=(self.ip, self.port), authkey=self.authkey)  # 管理者的IP，密码
        manger.start()  # 开启
        task, result =  manger.get_task(),  manger.get_result()  # task,任务，resulit结果

        for url in self.tasklist:
            print("task加入数据", url)
            task.put(url)  # 压入结果


        print("开始等待结果")


        for i in range(len(self.tasklist)):
            myresult = result.get(timeout=50)
            print("抓取到数据", myresult)
        manger.shutdown()  # 关闭服务器

'''
if __name__=="__main__":
    multiprocessing.freeze_support()  # 开启分布式支持
    urllist = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%95%B0%E6%8D%AE&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E6%B5%8B%E8%AF%95&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20web&p=1&isadv=0",
               "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%20%20%E8%BF%90%E7%BB%B4&p=1&isadv=0"]
    MySever=MainSever("10.0.123.119",8848,urllist,b"123456")
    MySever.runsever()  #服务器开启
'''
