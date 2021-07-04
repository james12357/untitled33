import time


class bank:

    def __init__(self):
        self.__cards = {"623887": ["111222", 100], "768875": ["167158", 200]}
        self.__card = ""
        self.__passwd = 0
        self.__logfile = open("log.txt", "a", encoding="utf-8")

    def __str__(self):
        return "[Object bank]"

    def __log(self, message: str):
        self.__logfile.write("[%s]%s\n" % (time.asctime(time.localtime(time.time())), message))
        self.__logfile.close()
        self.__logfile = open("log.txt", "a", encoding="utf-8")

    def login(self):
        self.__card = str(input("卡号>"))
        self.__passwd = input("密码>")
        if self.__card in self.__cards:
            if self.__passwd == self.__cards[self.__card][0]:
                self.__log(self.__card + " successfully login")
                return [True]
            else:
                self.__log(self.__card + " passwd not match")
                return [False]
        else:
            self.__log("user not match")
            return [False]

    def purchase(self, money: float or int):
        self.__cards[self.__card][1] += money
        self.__log(self.__card + " purchase " + str(money))
        return True

    def getMoney(self):
        self.__log(str(self.__card) + " successfully get money " + str(self.__cards[self.__card][1]))
        return self.__cards[self.__card][1]

    def takeMoney(self, amount: float or int):
        if amount < self.getMoney():
            self.__cards[self.__card][1] -= amount
            self.__log(str(self.__card) + " successfully take money " + str(amount))
            return True
        else:
            return False


main = bank()

if main.login()[0]:
    while True:
        a = int(input("请选择功能：\n1.查询余额\n2.存款\n3.取款\n>"))
        if a == 1:
            print(main.getMoney())
        elif a == 2:
            tmp = main.purchase(float(input("存额>")))
            if tmp:
                print("存款成功,当前余额" + str(main.getMoney()))
        elif a == 3:
            if main.takeMoney(float(input("取额"))):
                print("取钱成功")
