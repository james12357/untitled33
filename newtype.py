import hashlib


class bank:
    def __init__(self):
        self.__cards = {90000: ["8cb2237d0679ca88db6464eac60da96345513964", 100]}
        self.__passwd = 0

    def log(self):
        pass

    def login(self):
        while True:
            self.__card = input("卡号>")
            self.__passwd = input("密码>")
            if self.__card in self.__cards:
                if hashlib.new("sha1", self.__passwd.encode("utf-8")) == self.__cards[self.__card][0]:
                    return True

    def purchase(self):
        pass

    def getmoney(self):
        pass
