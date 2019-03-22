import re
from urllib import request
#断点调试
#beautiful Soup,scrapy两个框架
#爬虫 ，反爬虫，反反爬虫
#ip封
#代理ip库
class Spider():
    url='https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7qe1lmcs6uv'
    #非贪婪模式加（）之后则不包含界限范围的标签
    root_pattern='<div class="video-info">([\s\S]*?)</div>'
    name_pattern='</i>([\s\S]*?)</span>'
    number_pattern='<i class="ricon ricon-eye"></i>([\s\S]*?)</span>'
    
    def __fetch_content(self):
        r=request.urlopen(Spider.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_pattern,html)
            anchor={'name':name[0],'number':number}
            anchors.append(anchor)
        return anchors
#2.数据精炼refine
    def __refine(self,anchors):
        l=lambda anchor:{
            'name':anchor['name'].strip(),
            'number':anchor['number'][0]
            }
        return map(l,anchors)

#3.业务处理（排序）
    def __sort(self,anchors):
        anchors=sorted(anchors,key=self.__sort__seed,reverse=True)
        return anchors
    
    def __sort__seed(self,anchor):
        r=re.findall('\d*',anchor['number'])
        number=float(r[0])
        if '万' in anchor['number']:
            number*=10000
        return number

    def __show(self,anchors):
        # for anchor in anchors:
        #     print(anchor['name']+'-----'+anchor['number'])
        for rank in range(0,len(anchors)):
            print('rank '+str(rank+1)+':'+anchors[rank]['name']+anchors[rank]['number'])

    def go(self):
        htmls=self.__fetch_content()
        anchors=self.__analysis(htmls)
        anchors=list(self.__refine(anchors))
        anchors=self.__sort(anchors)
        self.__show(anchors)        

spirder=Spider()
spirder.go()
