# a=1
# b=2
# c=3
# a,b,c=1,2,3
# d=1,2
# a,b,c=d
# print(type(d))
# print(a)
# a=b=c=1
# print((b))
def a_b(name,gender='男',age=18,college='光明小学'):
    print('我的名字是：'+name)
    print('我的性别是：'+gender)
    print('我的年龄是：'+str(age))
    print('我的学校是：'+college)

a_b('sdfsdf')
print('``````````')
a_b('aaa','女',age=17,'dfa')