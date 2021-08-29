import requests
import re

url = "https://movie.douban.com/chart"
headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
           "Safari/537.36"}


def get() -> list:
    result = requests.get(url, headers=headers).text
    pattern = re.compile('<a.*?nbg.*?title="(.*?)">', re.S)
    stars_pattern = re.compile('span.*?rating_nums.*?>(.*?)<')
    url_pattern = re.compile('<a.*?nbg.*?href="(.*?)"')
    items = re.findall(pattern, result)
    stars = re.findall(stars_pattern, result)
    urls = re.findall(url_pattern, result)
    return list(zip(items, stars, urls))


if __name__ == "__main__":
    res = get()
    print(res)
