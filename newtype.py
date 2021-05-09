import hashlib


class bank:
    def __init__(self):
        self.__cards = {90000: ["8cb2237d0679ca88db6464eac60da96345513964", 100]}
        self.__passwd = 0

    def __log(self, message):
        pass

    def login(self):
        self.__card = input("卡号>")
        self.__passwd = input("密码>")
        if self.__card in self.__cards:
            if hashlib.new("sha1", self.__passwd.encode("utf-8")) == self.__cards[self.__card][0]:
                self.__log(self.__card)
                return [True, self.__card, self.__cards[self.__card][1]]

    def purchase(self, mone):
        if "int" in type(mone):
            self.__cards[self.__card][1] += mone
            self.__log("存款")
            return True
        else:
            return False

    def getmoney(self):
        return self.__cards[self.__card][1]

main = bank()
mess = main.login()
if mess[0]:
    while True:
        a = int(input("请选择功能：\n1.查询余额\n2.存款\n3.查询"))
        if a == 1:
            main.getmoney()
        elif a == 2:
            if main.purchase(input("存额>")):
                print("存款成功,当前余额" + main.getmoney())



