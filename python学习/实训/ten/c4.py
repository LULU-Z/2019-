#数量词
import re
a='python1111java6789php'
r=re.findall('[a-z]{3,7}?',a)
print(r)