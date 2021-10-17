# Failed
# noinspection PyCompatibility
from tkinter import Tk, Button, GROOVE
import os
from itertools import cycle


def show(command: str):
    """
    Execute a command in shell.
    :param command: command to do
    """
    os.system("start %s" % command)


command_dict = {"显示": "ms-settings:display", "存储": "ms-settings:storagesense",
                "Wi-Fi": "ms-settings:network-wifi", "VPN": "ms-settings:network-vpn",
                "桌面背景": "ms-settings:personalization-background",
                "主题": "ms-settings:themes", "开始菜单": "ms-settings:personalization-start",
                "账户": "ms-settings:emailandaccounts", "登录方式": "ms-settings:signinoptions",
                "更新": "ms-settings:windowsupdate", "备份": "ms-settings:backup",
                "关于": "ms-settings:about"}
a = cycle(list(command_dict))
root = Tk()
root.title("test")
root.resizable(width=True, height=True)
for x1 in range(1, 4):
    for y1 in range(1, 5):
        a1 = next(a)
        print(command_dict[a1])
        button = Button(command=lambda x=x1, y=y1: show(command_dict[a1]), width=20, height=3, relief=GROOVE, text=a1,
                        font=7, bd=5)
        button.grid(column=x1, row=y1)

root.mainloop()
