"""
@author:蔡俊熙
@license:MIT
"""
__all__ = ["dictGenerator", "getPlatform", "generateUnicodePassword"]


def dictGenerator(**kwargs):
    return kwargs


def getPlatform():
    return __import__("sys").platform


def generateUnicodePassword(length: int):
    passwd = []
    tmp = ""
    import random
    while True:
        try:
            for i in range(length):
                passwd.append(chr(random.randint(1, 65536)))
            print("".join(passwd))

        except UnicodeEncodeError:
            passwd = []
        else:
            for j in passwd:
                tmp += str(ord(j))
            print(tmp, end="")
            print()
            break
    return {"origin": "".join(passwd), "num": tmp}
