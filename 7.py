intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "dgblqvfswyjhtixpoemrcazknu"
a = input("1")
str = input("2")
if a == "1":
    trantab = str.maketrans(intab, outtab)
    print(str.translate(trantab))
else:
    trantab = str.maketrans(outtab, intab)
    print(str.translate(trantab))
