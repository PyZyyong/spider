#coding:utf-8

import threading
import Control.task.task
class taskQueue_base(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue  #队列

    def addtask(self, task):
        self.queue.put(task) #往队列加入任务

    def run(self):
        while True:
            mylist = self.queue.get()
            print(mylist)
            mytask = Control.task.task.Task(mylist[0],mylist[1],mylist[2],mylist[3])
            mytask.start()  # 开启
            mytask.join()