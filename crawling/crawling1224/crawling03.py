from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "sj6IFFPTvDc6xIf6Z8WTNftwtXOiQjkW7F3BMDI6DTMwoNCk%2FZJ3ANETMv29xBYKkt7y3EZpX1%2FNMhdJkXE7dQ%3D%3D"

Q0 = quote("서울특별시")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "10"
pageSize = "10"

paramset = "serviceKey=" + serviceKey + "&Q0=" + Q0 + "&Q1=" + "&ORD" +ORD + "&pageNo=" + pageNo + \
           "&startPage=" + startPage + "&numOfRows" + numOfRows + "&pageSize=" +pageSize

url = endpoint + paramset
print("url : " +url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")

for item in items:
    tagged_item = item.find("dutyname")
    print(tagged_item)