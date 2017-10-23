#coding:utf-8
import  matplotlib.pyplot as plt  #数据可视化
import matplotlib

class  DataView_Base:
    def __init__(self,numberlist,namelist):
        self.numberlist=numberlist
        self.namelist=namelist
        #matplotlib.use("Agg")  # 保存图片
        matplotlib.rcParams["font.sans-serif"] = ["simhei"]  # 解决中文字体
        matplotlib.rcParams["font.family"] = "sans-serif"

    def draw(self):
        pass
    def __del__(self):
        plt.close(0)
    def  show(self):
        plt.show()
    def save(self,path):
        plt.savefig(path)

