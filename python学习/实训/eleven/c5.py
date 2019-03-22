def f1():
    a=10
    def f2():
        a=20
        print(a)
    print(a)
    f2()
    print(a)

f1()

