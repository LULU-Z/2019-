# 概括字符集
# \d \D
# \w单词字符 \W
# \s空白字符 \S
# .匹配除换行符\n之外其他所有字符
import re
a='python  1111&*()java6789php'
r=re.findall('\S',a)
print(r)
