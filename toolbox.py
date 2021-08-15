"""
Some tools.
@author:蔡俊熙
@license:MIT
"""
__all__ = ["dictGenerator", "getPlatform", "generateUnicodeCharacters", "generateRandomCharacters"]


def dictGenerator(**kwargs):
    return kwargs


def getPlatform():
    return __import__("sys").platform


def generateUnicodeCharacters(length: int = 6):
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
    string = memoryview(bytes(string, "utf-8"))
    return string.hex(sep) if sep != "" else string.hex()


def generateRandomCharacters(length: int = 6):
    import random
    return (''.join(
        random.choice('ahui0-]}{?lubfGYUIABVEIIYYHULIAYUIIAWYAGO'
                      'UGAUSHIuityrtwtbyui,xmjnhcgbd9456!@#$%^'
                      '&*(526478253674][][') for i in range(length)))
