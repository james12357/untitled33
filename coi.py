"""
小楷想使用tkinter实现10秒倒计时的效果， 代码没有报错， 但是出现了问题，
你能找到问题在哪儿并且改正吗？
"""

import tkinter as tk

t = 10
# 创建窗口， 设置标题
root = tk.Tk()
root.title('倒计时')


# 定义函数， 改变标签内容实现倒计时
def timer():
    global t
    roll_value.set(str(t))
    t -= 1
    if t >= 0:

        root.after(1000, timer)
    else:
        roll_value.set('时间到!')


# 创建StringVar对象
roll_value = tk.StringVar(value='倒计时')

# 设置标签创建标签并且摆放
roll_label = tk.Label(textvariable=roll_value, width=10, height=4, background='light blue', font='楷体 -40 bold',
                      foreground='black')
roll_label.place(x=0, y=0)

timer()
root.mainloop()


