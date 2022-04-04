import subprocess
import sys
import os
processes_lst = []
while True:
    raw = input("$")
    sp = raw.split(" ", 1) if " " in raw else [raw]
    prog_name = sp[0]
    if len(sp) > 1:
        args: dict = eval(sp[1])
    else:
        args: dict = {}

