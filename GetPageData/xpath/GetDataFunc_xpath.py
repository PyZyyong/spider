#coding:utf-8
import lxml
import lxml.etree
import re
def  get_zhaopin(pagedata):
    numbers=-1
    mytree = lxml.etree.HTML(pagedata) #必须是网页原来的数据，转码失败
    worknumbers=mytree.xpath("//*[@class='search_yx_tj']/em/text()")
    numbers=eval(worknumbers[0].strip())
    return numbers

def  get_51job(pagedata):
    numbers=-1
    mytree = lxml.etree.HTML(pagedata)  # 必须是网页原来的数据，转码失败
    worknumbers = mytree.xpath("//*[@class='rt']/text()")
    regex = re.compile("\d+", re.IGNORECASE)
    mylist = regex.findall(worknumbers[0].strip())
    numbers=eval(mylist[0])
    return numbers