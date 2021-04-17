
a = "1"
b = 1
c = 0

i = 1


def cal(a):
    d = True

    def cc():
        try:
            a = input("请输入第一个数字:")
            d = (float(a) + float(i))
        except ValueError:
            print("输入错误!")
            return cc()

    cc()

    while d:
        try:
            b = input("请继续输入数字:")
            c = (int(a) + int(b))

            print("{0}加{1}等于{2}".format(a, b, c))
            a = c
        except ValueError:
            print("输入错误!")


try:
    cal(a)
except BaseException:
    print("退出方式异常!")
except OSError:
    print("系统错误!")
else:
    print("执行完成!")
