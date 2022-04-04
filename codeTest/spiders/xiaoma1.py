import requests
import json
url = "https://api.kids-creative.com.cn/v1/student/student/comment/list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50 "
}

data = {"params": {}, "program_id": 21505, "page_no": 1, "page_size": 10}
res = requests.post(url=url, headers=headers, data=json.dumps(data))
res = res.json()
for i in res["data"]["items"]:
    print(i["user"]["nickname"], i["content"])

