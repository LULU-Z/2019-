# CONDITION=True
# counter=0
#递归
# while counter <= 10:
#     counter +=1
#     print(counter)
# else:
#     print('EOF')

#主要用来遍历/循环 序列或者集合、字典
# a = [['apple','orange','banana','grape'],(1,2,3)]
# for x in a:
#     if 'apple' in x:
#         break
#     for y in x:
#        if y=='orange':
#            break
#        print(y)
# else:
#     print('fruit is gone')

# a=[1,2,3]
# for i in a:
#     if i==2:
#         continue
#     print(i)
# else:
#     print('EOF')

# for x in range(10,0,-2):
#     print(x,end=" | ")


a=[1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end=" | ")

b=a[0:len(a):2]
print(b)
