#coding:utf-8
import GetPageData.regex.GetDataFromPage_re
import GetpageSource.selenium.GetPageSourceChrome
import GetPageData.regex.GetDataFunc_re


mypage=GetpageSource.selenium.GetPageSourceChrome.GetPageSourceChrome("http://search.51job.com/list/010000%252C00,000000,0000,00,9,99,"+"python"+",2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")
mydata=mypage.getsource()
myget= GetPageData.regex.GetDataFromPage_re.GetDataFromPage_re(mydata, GetPageData.regex.GetDataFunc_re.get_51job) #第一个数据，第二个函数
print myget.getnumbers()