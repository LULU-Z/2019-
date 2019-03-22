import re
s='A83C7D1D8E67'
#match 和 search 只会匹配一次
#findall会匹配所有符合要求的字符串
r1=re.match('\d',s)
r2=re.search('\d',s)
r3=re.findall('\d',s)
print(r1)
print(r2.group())
print(r3)