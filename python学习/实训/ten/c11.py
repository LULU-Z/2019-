import re
s='life is short,i use python, i love python'
r=re.search('life(.*)python(.*)python',s)
# r1=re.findall('life(.*)python',s)
#0是默认的取值
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(0,1,2))
print(r.groups())
# print(r1)