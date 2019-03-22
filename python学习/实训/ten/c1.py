import re

a='C0C++8Java4C#5Python2Javascript'
r=re.findall('\d',a)
print(r)
# print(a.index('Python')>-1)