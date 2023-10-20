from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'cookie': 'SINAGLOBAL=1892350541392.0693.1648883392324; ALF=1724725305; SUB=_2AkMTse6Zf8NxqwJRmP4TzmPkaYx0zAnEieKl7R9CJRMxHRl-yT9vqkUJtRB6ODHAd1f7oAECrTIwRDuK9TSlw0UX-HMd; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhsMhXyzzcgI5Dacnqncu5S; _s_tentry=passport.weibo.com; Apache=8121425787260.876.1693278640812; ULV=1693278640830:1:1:1:8121425787260.876.1693278640812:; PC_TOKEN=00345f56b4; UOR=,,cn.bing.com'
}
r = requests.get("https://s.weibo.com/top/summary/", headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
s = soup.find_all("td", attrs={'class': 'td-02'})
resou = []
typeo = []
for i in s:
    resou.append(i.find("a").get_text())
s = soup.find("tbody")
s = s.find_all("td", attrs={'class': 'td-03'})
for i in s:
    try:
        typeo.append(i.find("i").get_text())
    except AttributeError:
        typeo.append("")
        continue
res = []
for i in range(0, len(resou)):
    res.append(str(i) + " " + resou[i] + " " + typeo[i])
print(res)


def getWbRs():
    return [resou, typeo]
