import re
from urllib import request
from bs4 import BeautifulSoup

class Sh():
    url='https://www.sge.com.cn/hqsj'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    # name_pattern='<td class="insid" height="40" id="myinstid" width="85">([\s\S]*?)</td>'

    def __fetch_content(self):
        rq=request.Request(Sh.url,headers=Sh.header)
        res=request.urlopen(rq)
        htmls=res.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        anchors=[]
        soup = BeautifulSoup(htmls,"lxml")
        a=soup.find_all(class_="ininfo")
        for AgAu in a:
            name=AgAu.find_all(class_="insid")
            price=AgAu.find_all("td")
            anchor={'name':name[0].string,'开盘价':price[1].string,'收盘价':price[2].string,'最高价':price[3].string,'最低价':price[4].string}
            anchors.append(anchor)
        # print(anchors)
        return anchors
    
    def __refine(self,anchors):
        l=lambda anchor:{
            'name':anchor['name'],
            '开盘价':anchor['开盘价'],
            '收盘价':anchor['收盘价'],
            '最高价':anchor['最高价'],
            '最低价':anchor['最低价']
            }
        return map(l,anchors)

    def __show(self,anchors):
        
        # for anchor in anchors:
        #     print(anchor['name']+'-----'+anchor['number'])
        print('序号'+'      '+'名字'+'          开盘价'+'         收盘价'+'         最高价'+'        最低价')
        for rank in range(0,len(anchors)):
            print(str(rank+1)+':'+'     '+"{: ^9}".format(anchors[rank]['name'])+'      '+"{: ^9}".format(anchors[rank]['开盘价'])+'      '+"{: ^9}".format(anchors[rank]['收盘价'])+'      '+"{: ^9}".format(anchors[rank]['最高价'])+'      '+"{: ^9}".format(anchors[rank]['最低价']))
            
    def go(self):
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=list(self.__refine(anchors))
        self.__show(anchors)
        # print(type(anchors))
        # print(anchors)


sh=Sh()
sh.go()