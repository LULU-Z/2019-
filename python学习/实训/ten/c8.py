import re 
lanuage='PythonC#JavaC#PHPC#'
def convert(value):
    matched=value.group()
    return '!!'+matched+'!!'
#4~8
# r=re.findall('c#.{3}',lanuage,re.I|re.S)
r=re.sub('C#',convert,lanuage,1)
# r=lanuage.replace('C#','GO')
print(r)

