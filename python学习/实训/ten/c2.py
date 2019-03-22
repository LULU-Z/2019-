# 字符集
import re 
s='abc,acc,adc,aec,afc,ahc'
r=re.findall('a[c-f]c',s)
print(r)