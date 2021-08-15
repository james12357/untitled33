"""
A screen saver.
@author:James
@license:MIT
"""
from tkinter import Tk, PhotoImage, Canvas, Label, BOTH
from itertools import cycle
import time
from os import listdir

imageList = cycle(listdir("src"))
root = Tk()
root.title("test")
root.resizable(width=True, height=True)
root.state("zoomed")
root.attributes('-fullscreen', True)
root.attributes("-topmost", True)
wid = root.winfo_screenwidth()
hei = root.winfo_screenheight()
canvas = Canvas(root, width=wid, height=hei, bg="yellow")
canvas.place(x=0, y=0)
image = PhotoImage(file="src/%s" % (next(imageList)))
canvas.create_image(0, 0, image=image)
aDict = {"Monday": "一", "Tuesday": "二", "Wednesday": "三",
         "Thursday": "四", "Friday": "五", "Saturday": "六", "Sunday": "日"}


def change():
    global image
    image = PhotoImage(file="src/%s" % (next(imageList)))
    canvas.create_image(0, 0, image=image)
    canvas.create_text(wid / 2, hei / 2 - 100,
                       text=time.strftime(" %H:%M\n星期{0}".format(aDict[time.strftime("%A", time.localtime())]),
                                          time.localtime()), font=("微软雅黑", 30), fill="white")
    canvas.after(2000, change)


root.bind("<Key>", exit)
root.bind("<Motion>", exit)
change()
root.mainloop()
