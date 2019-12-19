import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

newsnow_txarea = bs_obj.findAll("ul", {"class":"mlist2 no_bg"})
lis = newsnow_txarea[2].findAll("li")


for li in lis:
    strong = li.find("strong")
    print(strong.text)

