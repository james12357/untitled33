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
"""

import requests
import getopt
import sys

url = []
isFile = False
timeout = 10
mode = "r"

if len(sys.argv) > 1:
    opts, args = getopt.getopt(sys.argv[1:], "hf:t:", ["help", "filename=", "timeout="])
    for optName, optValue in opts:
        optValue: str
        if optName in ("-h", "--help"):
            pass
        if optName in ("-f", "--filename"):
            url = open(optValue, mode=mode, encoding="utf-8").readlines()
            isFile = True
        if optName in ("-t", "--timeout"):
            timeout = float(optValue)
    if args and not isFile:
        url = args
else:
    print(__doc__)
for i in url:
    try:
        result = requests.get(i, timeout=timeout)

    except Exception:
        print(f"[FAIL] {i}")
    else:
        code = str(result.status_code)
        if code[0] == "2":
            print(f"[OK] {result.url}")
        elif code[0] == "3":
            print(f"[WARN] {result.url}")
        elif code[0] == "4":
            print(f"[ERR] {result.url}")
