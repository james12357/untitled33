import random
import tkinter
from tkinter import Tk, GROOVE, Button, Label, TOP, messagebox
from itertools import cycle
from random import choice, shuffle

global running
nlst = ['蔡靖谦', '曾菲菲', '陈可欣', '陈兰熙', '陈粤军', '陈姿晴', '程正宇', '邓悠然', '范子阳', '胡雅菁', '胡梓豪', '黄佳琪', '黄诗淇', '黄智谦', '蒋乐敏', '雷雨聋', '金羿潼', '李博琛', '李晨瑜', '李浩源', '李晋炜', '刘立晨', '刘伟宏', '刘子辰', '马羽汝', '邵怡宣', '邵吟秋', '佘雨辰', '侣岩', '苏天政', '唐嘉怡', '万羽涵', '王博铭', '王浩翔', '王凯鑫', '王梓沛', '文冠铭', '文婉婷', '吴炯乐', '吴明珊', '肖星雨', '徐菁', '许轶菲', '杨睿杰', '易憋', '张瑛', '赵安南', '赵弘熙', '周显忠', '周洋']
random.shuffle(nlst)
names = cycle(nlst)
root = Tk()
root.title(' 滚 动 抽 奖 器')
txt = tkinter.StringVar()
start_label = Label(textvariable=txt, width=17, height=3,
                    background='light blue', font='楷体 -40 bold', foreground='black')
start2_label = Label(text='幸运儿是你吗...', width=17, height=3,
                     background='green', font='楷体 -40 bold', foreground='black')
tkinter.messagebox.showinfo("Success!", "Shuffled list: " + str(nlst))


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


def reload():
    root.destroy()
    import a


start_button = Button(text="开始", font="楷体 -40 bold", background="orange",
                      relief=GROOVE, command=start)
stop_button = Button(text="结束", font="楷体 -40 bold", background="orange",
                     relief=GROOVE, command=stop)
reload_button = Button(text="Same person all the time?", font="楷体 -24 bold", background="orange",
                       relief=GROOVE, command=reload)
start_label.pack(side=TOP)
start2_label.pack(side=TOP)
start_button.pack(side=TOP)
stop_button.pack(side=TOP)
reload_button.pack(side=TOP)
root.mainloop()
