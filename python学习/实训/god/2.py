import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        # r.raise_for_status()#如果状态不是200，引发HTTPError异常
        # print(r.raise_for_status())
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__=="__main__":
    url='http://www.baidu.com'
    print(getHTMLText(url))
# r=requests.get('http://www.baidu.com')
# print(r.status_code)
# # r.encoding='utf-8'
# # print(r.text)
# print(r.apparent_encoding)