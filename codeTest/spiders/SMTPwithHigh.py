from email.mime import text as txt
from email.header import Header
import smtplib
import doubanSpiderHigh as doubanHigh
import doubanSpiderNew as doubanNew


receiver = ["caijunxi@jamesnet.xyz", "501989869@qq.com"]
resHigh = doubanHigh.get()
resNew = doubanNew.get()
rHigh = []
user = "jamesoutmail@vip.qq.com"
server = "smtp.qq.com"
subject = "今日豆瓣榜单"
for i in resHigh["subjects"]:
    rHigh.append((i["title"], i["rate"], i["url"]))
rHigh = sorted(rHigh, key=lambda k: k[1], reverse=True)
resNew = sorted(resNew, key=lambda k: k[1], reverse=True)
prv = ""
prv += "豆瓣新片榜\n"
for j in rHigh:
    prv += f"电影：{j[0]}，评分：{j[1]}，链接：{j[2]}\n\n"
prv += "豆瓣高分榜\n"
for j in resNew:
    prv += f"电影：{j[0]}，评分：{j[1]}，链接：{j[2]}\n\n"
text = txt.MIMEText(prv, "plain", "utf-8")
text["Subject"] = Header(subject, "utf-8")
text["From"] = Header("测试", "utf-8")

obj = smtplib.SMTP_SSL(host=server)
obj.connect(host=server, port=465)
obj.login(user=user, password="hcktfiqkjquzdicb")
obj.sendmail(user, receiver, text.as_string())
