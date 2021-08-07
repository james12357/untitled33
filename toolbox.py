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
    import random
    passwd = []
    num = ""
    while True:
        try:
            for i in range(length):
                passwd.append(chr(random.randint(1, 65536)))
            for j in passwd:
                num += str(ord(j))
        except UnicodeEncodeError:
            passwd = []
        else:

            break
    return {"origin": "".join(passwd), "num": num}


def calculateHexFromString(string: str or bytes, sep: str = ""):
    string = memoryview(bytearray(string))
    return string.hex(sep) if sep != "" else string.hex()
