from ctypes import windll


def lock_windows():
    user32 = windll.LoadLibrary("user32.dll")
    user32.LockWorkStation()


lock_windows()
