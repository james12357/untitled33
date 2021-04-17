((lambda x: x)("f"))
while True:
    a = int(input("sum"))
    i = 2
    print((lambda x: x)("加载中..."))


    def f(argument):
        for counter in range(i, argument - 2):
            if argument % i == 0:
                print("合数")
                exit(0)
            counter += 1
        print("质数")


    f(a)
