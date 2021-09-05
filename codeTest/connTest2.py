import socket  # 导入 socket 模块
import _thread

count = 0


def a():
    while True:
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12346  # 设置端口号
        s.connect((host, port))
        print(s.recv(1024))
        s.close()


_thread.start_new_thread(a, ())
_thread.start_new_thread(a, ())
_thread.start_new_thread(a, ())
_thread.start_new_thread(a, ())
_thread.start_new_thread(a, ())
_thread.start_new_thread(a, ())
while True:
    pass
