import re
# *匹配0次或者无限多次
# +匹配1次或者无限多次
# ?匹配0次或者1次
a='pytho1python2pythonn2'
r=re.findall('python{1,2}?',a)
print(r)