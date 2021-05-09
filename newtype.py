


class bank:
    def __init__(self):
        self.__cards = {"90000": ["12345", 100]}
        self.__passwd = 0

    def __log(self, message):
        pass

    def login(self):
        self.__card = str(input("卡号>"))
        self.__passwd = input("密码>")
        if self.__card in self.__cards:
            if self.__passwd == self.__cards[self.__card][0]:
                self.__log(self.__card)
                return [True]
            else:
                return [False]
        else:
            return [False]

    def purchase(self, mone):
        if type(1.0) == type(mone):
            self.__cards[self.__card][1] += mone
            self.__log("存款")
            return True
        else:
            return False

    def getmoney(self):
        return self.__cards[self.__card][1]
    def takemoney(self, amount):
        if amount < self.getmoney():
            self.__cards[self.__card][1] -= amount
            return True

main = bank()
mess = main.login()

if mess[0]:
    while True:
        a = int(input("请选择功能：\n1.查询余额\n2.存款\n3.取款"))
        if a == 1:
            print(main.getmoney())
        elif a == 2:
            tmp = main.purchase(float(input("存额>")))
            if tmp:
                print("存款成功,当前余额" + str(main.getmoney()))
        elif a == 3:
            if main.takemoney(float(input("取额"))):
                print("取钱成功")




