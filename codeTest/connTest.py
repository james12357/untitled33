import socket  # 导入 socket 模块
import _thread
import time

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12346  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接


def f(k, p):
    while True:
        try:
            c, address = s.accept()  # 建立客户端连接
            print(address)
            c.send(open("dist/var11.exe", "rb").read())
            print(f"Parent:{k}, Child:{p}")
            c.close()
        except MemoryError:
            print("警告！内存不足！")
        except Exception:
            pass


def run(q):
    for h in range(20):
        _thread.start_new_thread(f, (q, h))


for i in range(18):
    _thread.start_new_thread(run, (i,))

while True:
    pass
