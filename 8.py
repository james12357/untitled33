print("虚拟服务器在端口 8899 已开启。\npython正在运行...")
a = []
b = input("行数")
for counter in b:
    if not len(a) == 0:
        a.append(int(a[len(a)-2] + 1))
    else:
        a.append(1)
    print(a)
    print("\n")
