#coding:utf-8
import re
def  get_zhaopin(pagedata):
    numbers=0
    restr = """<em>(\\d+)</em>"""  # 正则表达式
    regex = re.compile(restr, re.IGNORECASE)  # 预编译正则
    temp = regex.findall(pagedata)  # 寻找所有
    numbers = eval(temp[0])
    return numbers

def  get_51job(pagedata):
    numbers=-1

    #restr = """共(\\d+)条职位"""  # 正则表达式
    restr = "<div class=\"rt\">([\s\S]*?)</div>"
    regex = re.compile(restr, re.IGNORECASE)  # 预编译正则
    temp = regex.findall(pagedata)  # 寻找所有

    #print temp  # 打印
    laststr=temp[0].strip() #删除两端空格
    #print  laststr #  共5461条职位
    newrestr = "(\\d+)"
    regexnew = re.compile(newrestr, re.IGNORECASE)  # 预编译正则
    tempnew = regexnew.findall( laststr)  # 寻找所有
    print tempnew


    if  len(temp)>=1:
        pass
        numbers=eval(tempnew[0]) #返回整数
    else:
        print "抓取失败"


    return numbers