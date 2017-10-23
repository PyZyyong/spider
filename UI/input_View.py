#coding:utf-8

import Tkinter
import Tkinter

class InputView_Base(object):
    def __init__(self):
        self.win=Tkinter.Tk()
        self.win.geometry("600x300+0+0")
        self.win.title("BigdataFind")
        self.entry=Tkinter.Entry(self.win) #输入
        self.entry.place(x=0,y=0)
        self.button=Tkinter.Button(self.win,text="搜索",command=self.search)
        self.button.place(x=150,y=0)




    def show(self):
        self.win.mainloop()
    def search(self):
        print("click")
    def selectshowtype(self,*arg):
        self.showtype=self.comboxshowlist.get()
        print(self.showtype)


my=InputView_Base()
my.show()



