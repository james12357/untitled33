import tkinter
from tkinter import messagebox
loginSuccess: bool = False
noPassword = True
root = tkinter.Tk()
account = {"小花": "123456"}
user = tkinter.StringVar()
password = tkinter.StringVar()


def login():
    global loginSuccess
    if (user.get() in account and
            password.get() == account[user.get()]):

        messagebox.showinfo("成功", "登录成功！")
        loginSuccess = True
        root.destroy()
    else:
        messagebox.showinfo("失败", "失败")


def register():
    if user.get() in account:
        messagebox.showinfo("失败", "失败")

    else:
        account[user.get()] = password.get()
        messagebox.showinfo("成功", "注册成功！")


root.title("")
root.geometry("400x150")
tkinter.Label(root, text="账号", width=25, height=2).grid(row=0, column=0)
tkinter.Label(root, text="密码", width=25, height=2).grid(row=1, column=0)
tkinter.Entry(textvariable=user).grid(row=0, column=1)
tkinter.Entry(textvariable=password).grid(row=1, column=1)
tkinter.Button(text="登录", command=login).place(x=170, y=100)
tkinter.Button(text="注册", command=register).place(x=230, y=100)
root.mainloop()
