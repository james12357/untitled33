import os

o = lambda x: os.system(x)
a = {"ppt": "ppt", "pptx": "ppt", "doc": "doc"}
for i in a:
    o("move *.%s %s" % (i, a[i]))
o("pause")

