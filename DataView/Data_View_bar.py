#coding:utf-8
import  DataView.Data_View_Base
import  matplotlib.pyplot as plt  #数据可视化
import matplotlib


class DataView_bar(DataView.Data_View_Base.DataView_Base):
    def __init__(self,numberlist,namelist):
        DataView.Data_View_Base.DataView_Base.__init__(self,numberlist,namelist)
    def draw(self):
        for  i  in range(len(self.numberlist)):
            plt.bar([i], [self.numberlist[i]], label=self.namelist[i])
        matplotlib.use("Agg")
        plt.legend()

'''
numberlist=[1343,7156,1919 ,5928,1748 ]
namelist=[u"java",u"php中国",u"python",u"cpp",u"android"]
mybar=DataView_bar(numberlist,namelist)
mybar.draw()
mybar.save("1.jpg")
'''



#mybar.show()


