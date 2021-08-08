import tkinter
from tkinter import Tk, GROOVE, Button, Label, TOP, messagebox
from itertools import cycle

global running
names = cycle(["小明", "小红", "小军", "小花", "智慧老人"])
root = Tk()
root.title(' 滚 动 抽 奖 器')
txt = tkinter.StringVar()
start_label = Label(textvariable=txt, width=17, height=3,
                    background='light blue', font='楷体 -40 bold', foreground='black')
start2_label = Label(text='幸运儿是你吗...', width=17, height=3,
                     background='green', font='楷体 -40 bold', foreground='black')


def rolling():
    global running
    if running:
        root.after(50, rolling)
    else:
        return None
    txt.set(next(names))


def start():
    global running
    running = True
    stop_button.focus()
    rolling()


def stop():
    global running
    running = False
    start_button.focus()
    if messagebox.askokcancel("恭喜", f"恭喜 {txt.get()} 获得一等奖！\n按 确定 重新开始"):
        start()
    else:
        return None


start_button = Button(text="开始", font="楷体 -40 bold", background="orange",
                      relief=GROOVE, command=start)
stop_button = Button(text="结束", font="楷体 -40 bold", background="orange",
                     relief=GROOVE, command=stop)
start_label.pack(side=TOP)
start2_label.pack(side=TOP)
start_button.pack(side=TOP)
stop_button.pack(side=TOP)
root.mainloop()
