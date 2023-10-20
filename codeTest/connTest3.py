"""
Test connection from local to [urls].
usage:connTest3 [-t timeout] [-f filename] [url]
   or: connTest [-h]
   or: connTest
Arguments:
    -t or --timeout     Set timeout. Default is 10.
    -f or --filename    Set filename.*Will override urls*
    <arguments>         Set urls.
    -h or --help        Show help(This message)
    -a or --async       Test urls async.(Experimental)
"""

import requests
import getopt
import sys
import _thread

url = []
isFile = False
timeout = 10
mode = "r"
isAsync = False
lock = False
finishTime = 0
global i
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
               "Safari/537.36"}


def check(c):
    global lock, finishTime, headers
    try:
        result = requests.get(c, timeout=timeout, headers=headers)
    except Exception:
        while lock:
            pass
        lock = True
        print(f"[FAIL] {c}")
        finishTime += 1
        lock = False
    else:
        while lock:
            pass
        lock = True
        code = str(result.status_code)

        if code[0] == "2":
            print(f"[OK-{result.status_code}] {result.url} {result.elapsed.total_seconds() * 1000} ms")
        elif code[0] == "3":
            print(f"[WARN-{result.status_code}] {result.url} {result.elapsed.total_seconds() * 1000} ms")
        elif code[0] == "4":
            print(f"[ERR-{result.status_code}] {result.url} {result.elapsed.total_seconds() * 1000} ms")
        finishTime += 1
        lock = False


if len(sys.argv) > 1:
    opts, args = getopt.getopt(sys.argv[1:], "hf:t:a", ["help", "filename=", "timeout=", "async"])
    for optName, optValue in opts:
        optValue: str
        if optName in ("-h", "--help"):
            print(__doc__)
        if optName in ("-f", "--filename"):
            url = open(optValue, mode=mode, encoding="utf-8").readlines()
            for i in range(0, len(url)):
                if url[i][-1] == "\n":
                    url[i] = url[i][0:len(url[i]) - 1]
            isFile = True
        if optName in ("-t", "--timeout"):
            timeout = float(optValue)
        if optName in ("-a", "--async"):
            isAsync = True
    if args and not isFile:
        url = args
else:
    print(__doc__)
if isinstance(url, list) and not isAsync:
    for i in url:
        check(i)
elif not isAsync:
    check(url)
elif isinstance(url, list):
    for i in url:
        _thread.start_new_thread(check, (i,))
    while finishTime < len(url):
        pass
else:
    print("Invalid async option")
