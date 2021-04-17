'''
@author:蔡俊熙
'''
try:
    i = int(input("1"))
    a = int(input("2"))
    b = int(input("3"))
    ma = max(i, a, b)
    if i + a > ma and i + b > ma and a + b > ma:
        print("三角形成立，开始判断等腰三角形")
        if i == a or i == b or a == b:
            print("是等腰三角形")
        else:
            print("非等腰三角形")
    else:
        print("非三角形")
except ValueError:
    print("输入数据类型错误！")
