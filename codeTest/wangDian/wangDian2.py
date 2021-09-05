import tkinter
from tkinter import messagebox

from PIL import Image, ImageTk

import wangDian

if not wangDian.loginSuccess and not wangDian.noPassword:
    exit(1)
items = [["无人机", 5000, 0, 200, "颜色众多，星星、爱心图案\n牢固轻便，容量大\n", "./四轴无人机.png"],
         ["可爱手账", 300, 300, 200, "装置4000万像素摄像头\n20km稳定控制\n续航强，稳定，可受4级风力\n", "./礼物盒.jpg"],
         ["钢笔", 400, 600, 200, "送人必备，可定制姓名\n日本进口工艺，颜色简约大方\n", "./钢笔.png"]]

balance = 5000


class shoppingItem(object):
    def __init__(self, num: int):
        self.num = num
        self.text = tkinter.StringVar()
        self.name = items[num][0]
        self.price = items[num][1]
        self.x_pos = items[num][2]
        self.y_pos = items[num][3]
        self.icon = Image.open(items[num][5])
        self.icon = self.icon.resize((300, 300))
        self.icon = ImageTk.PhotoImage(self.icon)
        self.txt = items[num][4]
        self.text.set(f"{self.name}\n{str(self.price)}")
        self.button = tkinter.Button(
            image=self.icon, textvariable=self.text, compound=tkinter.TOP, command=self.buy)
        self.button.place(x=self.x_pos, y=self.y_pos)
        self.button.bind('<Enter>', self.enter)
        self.button.bind('<Leave>', self.leave)

    def enter(self, event):
        print(event)
        self.text.set(f"{self.txt}\n{self.price}")

    def leave(self, event):
        print(event)
        self.text.set(f"{self.name}\n{self.price}")

    def buy(self):
        global balance
        global infoTxt
        if balance >= self.price:
            balance -= self.price
            messagebox.showinfo("成功", "购买成功！")
            infoTxt.set(f"账号:{wangDian.user.get()}， \n余额:{balance}")
        else:
            messagebox.showinfo("失败", "余额不足！")


root2 = tkinter.Tk()
root2.geometry('900x700')
infoTxt = tkinter.StringVar()
infoTxt.set(f"账号:{wangDian.user.get()}， \n余额:{balance}")
tkinter.Label(text="小码精灵购物商城", width=18, height=3, background='light blue',
              font='楷体 -55 bold', foreground='black').place(x=0, y=0)
labUser = tkinter.Label(image=ImageTk.PhotoImage(Image.open("./用户.png").resize((150, 150)))).place(x=550, y=0)
labInfo = tkinter.Label(textvariable=infoTxt, font="楷体 -20 bold").place(x=700, y=0)
tkinter.Label(root2, text="欢迎", background="light blue").pack(side=tkinter.TOP)
item1 = shoppingItem(0)
item2 = shoppingItem(1)
item3 = shoppingItem(2)
root2.mainloop()
