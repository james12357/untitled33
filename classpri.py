import platform
import time
import sys
import hashlib

# main part
has = hashlib.sha1()
user = __import__("getpass").getuser()
localtime = time.asctime(time.localtime(time.time()))
print("Welcome back, " + user + "!")
print("Running on %s, %s, using python v%s" % (
    platform.platform(), platform.architecture()[0], platform.python_version()))
print("time: " + localtime)


class c:
    def __init__(self):
        self.__passwd = input("setpasswd>>")
        self.__realcode = input("code>>")
        self.__realname = input("name>>")
        self.__code = self.__realcode
        self.__name = self.__realname
        self.__hidecode = self.__code[0] + self.__code[-1]
        self.__hidename = self.__name[0] + self.__name[-1]
        self.__codestars = int(len(self.__code) - 2) * "*"
        self.__namestars = int(len(self.__name) - 2) * "*"
        self.__nowhash = hashlib.new("sha1", (self.__code[::2] + self.__name[::2] + self.__namestars).encode("utf-8"))\
            .hexdigest()

    def seta(self):
        if input("verify your original passwd>>") == self.__passwd:
            self.__passwd = input("set new passwd>>")
            self.__realcode = input("code>>")
            self.__realname = input("name>>")
            self.__code = self.__realcode
            self.__name = self.__realname
            self.__hidecode = self.__code[0] + self.__code[-1]
            self.__hidename = self.__name[0] + self.__name[-1]
            self.__codestars = int(len(self.__code) - 2) * "*"
            self.__namestars = int(len(self.__name) - 2) * "*"
            self.__nowhash = hashlib.new("sha1", (self.__code[::2] + self.__name[::2] + self.__namestars).encode(
                "utf-8")).hexdigest()

    def getname(self):
        if input("passwd>>") == self.__passwd:
            return self.__name
        else:
            print("not match")

    def getcode(self):
        if input("passwd>>") == self.__passwd:
            return self.__code
        else:
            print("not match")

    def gethidecode(self):
        return str(self.__hidecode[0]) + self.__codestars + str(self.__hidecode[1])

    def gethidename(self):
        return str(self.__hidename[0]) + self.__namestars + str(self.__hidename[1])

    def gethash(self):
        return self.__nowhash

    def verifyhash(self):
        if input("verify-hash>") == self.__nowhash:
            return True
        else:
            return False


a = c()
print(sys.getsizeof(a))
while True:
    n = input("s/gn/gc/e/ghc/ghn/gnh/vh>>")
    if n == "s":
        a.seta()
    if n == "gn":
        print(a.getname())
    if n == "gc":
        print(a.getcode())
    if n == "e":
        exit(0)
    if n == "ghc":
        print(a.gethidecode())
    if n == "ghn":
        print(a.gethidename())
    if n == "gnh":
        print(a.gethash())
    if n == "vh":
        print(a.verifyhash())
