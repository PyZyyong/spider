#coding:utf-8
import  Control.taskqueue.taskqueue
import Queue
if  __name__=="__main__":
    wordlist = ["python", "python 数据", "python 运维", "python 测试", "python 后端", "python web"]
    wordlist1 = [u"python", u"python 数据", u"python 运维", u"python 测试", u"python 后端", u"python web"]
    Emaillist = ["Zy_zyong@163.com"]

    try:
        queue = Queue.Queue(10)  # 任务队列最大容量为10
        mytaskqueue = Control.taskqueue.taskqueue.taskQueue_base(queue)  # 开启任务队列
        mytaskqueue.start()  # 队列开始执行
        mytaskqueue.addtask([120,wordlist,wordlist1,Emaillist])  # 增加任务
    except:
        pass




    '''
    wordlist = ["python", "python 数据", "python 运维", "python 测试", "python 后端", "python web"]
    wordlist1 = [u"python", u"python 数据", u"python 运维", u"python 测试", u"python 后端", u"python web"]
    Emaillist = ["yincheng8848@163.com", "18857566375@163.com"]
    mytask=Control.task.task.Task(120,wordlist,wordlist1,Emaillist )
    mytask.start()
    mytask.join()
    print "OK"
    '''


