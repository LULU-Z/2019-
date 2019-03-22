def f1():
    a=10
    def f2():
        #a被Python认为是一个局部变量
        # a=20
        # return a 
        c=a*10
        print('a')
    return f2
f=f1()
print(f)
print(f.__closure__)
