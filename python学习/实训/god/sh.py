import re
from urllib import request
from bs4 import BeautifulSoup

class Sh():
    url='http://www.sge.com.cn/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    
    # name_pattern='<tr class="ininfo">([\s\S]*?)</tr>'
    # name_pattern='<tr class="bt">[\s\S]*?</tr>'
    # name_pattern='<tr class="bt">\s</tr>'
    # name_pattern='<tbody>(.*?)</tbody>'
    name_pattern='<div id="tableinfo">[\s\S]*?</div>'

    def __fetch_content(self):
        rq=request.Request(Sh.url,headers=Sh.header)
        res=request.urlopen(rq)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        soup = BeautifulSoup(htmls,"lxml")
        a=soup.find_all("tr",class_="ininfo current")
        print(a)
    def go(self):
        htmls=self.__fetch_content()
        self.__analysis(htmls)

    

sh=Sh()
sh.go()

        