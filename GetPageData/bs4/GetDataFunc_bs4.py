#coding:utf-8
from  bs4 import BeautifulSoup
import re
def  get_zhaopin(pagedata):
    numbers=-1
    soup = BeautifulSoup(pagedata, "lxml", from_encoding="utf-8")  # 创建对象
    worknumbers = soup.find_all("span", class_="search_yx_tj")
    numbers=(eval(worknumbers[0].select("em")[0].get_text()))  #
    return numbers

def  get_51job(pagedata):
    numbers=-1
    soup = BeautifulSoup(pagedata, "lxml", from_encoding="utf-8")  # 创建对象
    worknumbers = soup.find_all("div", class_="rt")
    gettext = worknumbers[0].get_text().strip()

    regex = re.compile("\d+", re.IGNORECASE)
    mylist = regex.findall(gettext)
    numbers=eval(mylist[0])
    return numbers