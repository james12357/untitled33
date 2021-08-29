import requests
import json


def get() -> dict:
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0"
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
               "Safari/537.36"}
    result = requests.get(url, headers=headers).text
    return json.loads(result)


if __name__ == "__main__":
    for i in get()["subjects"]:
        print(i["title"])

