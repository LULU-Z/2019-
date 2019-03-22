# a=25
#闭包=函数+环境变量（函数定义时候）
#现场
def curve_pre():
    a=25
    def curve(x):
        return a*x*x
    return curve

f=curve_pre()
a=10
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))

