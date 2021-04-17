class s:
    def __init__(self):
        self.__username = "admin"
        self.__passwd = 998877

    def getuser(self):
        return self.__username

    def getpasswd(self):
        return self.__passwd


vd = s()


def validation(user, passwd):
    if vd.getuser() == user and vd.getpasswd() == passwd:
        return True
    else:
        return False


# Main part

for i in range(3):
    tmpu = input("%d chance(s) left,user>" % (3 - i))
    tmpp = input("%d chance(s) left,passwd>" % (3 - i))
    if validation(tmpu, tmpp):
        exit(0)
    else:
        print("输入错误")
print("已被锁定")
