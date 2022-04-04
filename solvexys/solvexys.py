from sympy import *
import inteligent_change


def ax1(equ):
    x = symbols('x')
    return solve(equ, x)  # x ** 2+2 * x + 1


def ax2(equ: list):
    x, y = symbols("x,y")
    return solve(equ, [x, y])


digits = 0
equation_for_2num = []
res = []
to_num = True if input("转换为小数请输入1[回车]，不转换请按[回车]") == "1" else False
if to_num:
    digits = int(input("保留几位小数>"))
number = int(input("元数[1/2]>"))
if number == 1:
    res = ax1(inteligent_change.change(input(">")))
    if to_num:
        for i in range(len(res)):
            res[i] = res[i].evalf(digits)
    print(res)
elif number == 2:
    for i in range(2):
        equation_for_2num.append(inteligent_change.change(input(f"输入第{i + 1}个方程")))
    res = ax2(equation_for_2num)
    if to_num:
        for i in res:
            res[i] = res[i].evalf(digits)
    print(res)
