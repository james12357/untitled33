import sys
fo = open("dics.txt", "r", encoding="utf-8")
lo = fo.readlines()
do = {}
for i in lo:
    tmp = i.split("|")
    tmp[1] = tmp[1].rstrip("\n")
    do[tmp[1]] = tmp[0]
c = open(sys.argv[1], mode="r", encoding="utf-8").read() \
    if len(sys.argv) > 1 \
    else ''.join(sys.stdin.readlines())

for i in do:
    c = c.replace(i, do[i])
print("-------")
exec(c)
