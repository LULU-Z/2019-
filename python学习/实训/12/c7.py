import time
def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print('This is a function'+func_name)

@decorator
def f2(fun_name1,fun_name2):
    print('This is a function'+fun_name1+fun_name2)
@decorator
def f3(fun_name1,fun_name2,**kw):
    print('This is a function'+fun_name1+fun_name2)
    print(kw)


f1("zuolulu")
f2('df','df.')
f3('asd','dfdf',a=1,b=2,c='123')
