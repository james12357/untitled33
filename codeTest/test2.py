from tkinter import Tk, Label, Entry, Button, TOP
import pymysql

cursor = pymysql.connect(host="localhost", user="root", passwd="123456").cursor()  # 初始化数据库连接
cursor.execute("use testdb")
root = Tk()  # 初始化窗口
root.title("QR Code Generator")
root.geometry("800x600")


def register():
    pass


lab1 = Label(root, text="请输入名字：", font=("微软雅黑", 18))
inp = Entry(root, width=50)
but = Button(root, text="注册", font=("微软雅黑", 18), command=register)
lab1.pack(side=TOP)
inp.pack(side=TOP)
but.pack(side=TOP)
root.mainloop()
