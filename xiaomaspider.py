import requests
import bs4
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.159 "
                  "Safari/537.36"
}

a = requests.get("https://ai.sandbox.kids-coding.com.cn/testsite/literature.html")
a.encoding = "utf-8"
a = a.text
soup = bs4.BeautifulSoup(a, "lxml")
b = soup.select("#root > div > div > div.body_container > div > div > div.book-content > div.summary")
for i in b:
    print(i)
