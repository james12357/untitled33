
import os
while True:
    a = input(">>>")
    print(str(os.system(a)).encode("GBK"))
