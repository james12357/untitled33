import requests
import getopt
import sys

url = ["http://baidu.com"]
timeout = 3

if len(sys.argv) > 1:
    opts, args = getopt.getopt(sys.argv[1:], "hf:t:u:", ["help", "filename=", "timeout=", "url="])
    for optName, optValue in opts:
        optValue: str
        if opts in ("-h", "--help"):
            # TODO(James): complete document
            pass
        if opts in ("-f", "--filename"):
            url = open(optValue, "r").readlines()
        if opts in ("-t", "--timeout"):
            timeout = float(optValue)
        if opts in ("-u", "--url"):
            url = optValue.split(" ")

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
