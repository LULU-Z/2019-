import re
from urllib import request
from bs4 import BeautifulSoup
import io
import sys
import codecs


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
class JD():
    url='https://search.jd.com/Search?keyword=%E9%87%91%E6%9D%A1&enc=utf-8&wq=%E9%87%91%E6%9D%A1&pvid=82c916a4bba3483e9c0e9278b574eba9'
    name_pattern='<em>([\s\S]*?)<font class="skcolor_ljg">'
    def __fetch_content(self):
        r=request.urlopen(JD.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        # print(type(htmls))
        return htmls
        # print(type(htmls))
        # f = codecs.open('JD.doc','w','utf-8')
        # f.write(htmls)
        # f.close
    
    def __analysis(self,htmls):
        anchors=[]
        soup = BeautifulSoup(htmls,"lxml")
        a=soup.find_all(class_='gl-warp clearfix')
        for AgAu in a:
            Price=AgAu.find_all(class_='p-price')
            for price in Price:
                print(price.i.string)
            Introduce=AgAu.find_all(class_='p-name p-name-type-2')
            for introduce in Introduce:
                # introduce1=introduce.find_all(name='em')
                introduce1=introduce.find_all(text=re.compile('黄金'))
                introduce2=introduce.find_all(name='em')
                introduce3=introduce.find_all(text=re.compile(JD.name_pattern))
                # introduce2=introduce.find_all()
                print(introduce1)
                print('-----------------------------------------')
                print(introduce2)
                print('*****************************************')
                print(introduce3)
            # introduce=AgAu.find_all(name='i')
            # print(introduce[1],'\n')
            # print(price)
        # print(a)
        # for AgAuin soup:
        #     name=AgAu.find_all(class_="inskcolor_ljg")
        #     print(name)
        
    def go(self):
        htmls=self.__fetch_content()
        self.__analysis(htmls)

jd=JD()    
jd.go()