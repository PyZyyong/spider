#coding:utf-8
import  matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云的模块
import jieba  #"我 今天 早上 吃饭 了"
import numpy as np
from PIL import Image #背景图

#背景图
background=np.array(Image.open("2.jpg"))
#打开文本
textfile=open("rsa.txt").read()
print textfile
#分词
wordlist=jieba.cut(textfile,cut_all=True)
space_split="".join(wordlist)
#构造词云
mywordclound=WordCloud(background_color="white",#背景
                       mask=background,#背景图片
                       max_words=20,
                       stopwords=STOPWORDS,
                       #font_path="C:/Windows/Boot/Fonts/chs_boot.ttf",
                       font_path="simkai.ttf",
                       max_font_size=440,
                       random_state=30,
                       scale=1
                       ).generate(space_split) #构造

image_color=ImageColorGenerator(background) #tupian 图片生成词云

#show
plt.imshow(mywordclound)
plt.axis("off")
plt.show()

