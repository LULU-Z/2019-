import time
def f1():
    # print(time.time())
    print('This is a function')
#时间戳
# f1()
def f2():
    print('This is two function')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)