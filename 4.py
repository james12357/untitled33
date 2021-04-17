
import sys
import os
a="1"
b=1
c=0
d="666"
i=1
def cal(a):

    try:
        a = input("请输入第一个数字:")
        d =(float(a) + float(i))
    except ValueError:
        print("第一个数输入错误,程序结束!")

        sys.exit(1)
    while True:
        try:
            b = input("请继续输入数字:")
            c = (float(a) / float(b))

            print("{0}除以{1}等于{2}".format(a, b, c))
            a = c
        except ValueError:
            print("输入错误!")
try:
    cal(a)
except BaseException:
    print("退出方式异常!")



