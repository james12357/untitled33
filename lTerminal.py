import os
import sys
import re
import subprocess
tmp_str = ""
paths: list = os.environ["PATH"].split(";")  # 获取可执行文件路径
ind: dict = {}  # 索引 键：路径 值：文件
envDict: dict = {}
for i in paths:
    try:
        ind[i] = "|".join(os.listdir(i))
    except FileNotFoundError:
        pass
jPattern = re.compile("java version \"(.*?)\"")
gPattern = re.compile("Your branch is up to date with '(.*?)'")
global cwd, cwd_files


def update_cwd():
    global cwd, cwd_files
    cwd = os.getcwd()
    cwd_files = "|".join(os.listdir(cwd))


update_cwd()


def find_file_in_path(name: str):
    for j in ind:
        if name in ind[j]:
            return True
    return False


# 初始化
# Python检测
if find_file_in_path("python.exe"):
    envDict["python"] = [True, f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"]
# java检测
if find_file_in_path("java.exe"):
    v = (" " + os.popen("java -version 2>&1").read())
    # print(v)
    envDict["java"] = [True, "v" + jPattern.findall(v)[0]]
# nodejs检测
if find_file_in_path("node.exe"):
    v = (" " + os.popen("node -v 2>&1").read())
    v = v.rstrip("\n").rstrip(" ")
    # print(v)
    envDict["nodejs"] = [True, v]
# 是否为git
if ".git" in cwd_files:
    v = (os.popen("git status 2>&1").read())
    envDict["git"] = [True, gPattern.findall(v)[0]]
print(envDict)
while True:
    if ".py" in cwd_files:
        tmp_str += f"|via Python {envDict['python'][1]}"
    if ".java" in cwd_files or ".class" in cwd_files:
        tmp_str += f"\n|via Java {envDict['java'][1]}"
    if ".py" in cwd_files:
        tmp_str += f"\n|via Nodejs {envDict['nodejs'][1]}"
    if envDict["git"][0]:
        tmp_str += f"\n|at branch {envDict['git'][1]}"
    print("|" + cwd)
    print(tmp_str)
    command = input("|$")
    s = subprocess.Popen(command, shell=True, encoding="utf-8")
    while s.poll() is None:
        pass
    command = ""
    tmp_str = ""
    update_cwd()
