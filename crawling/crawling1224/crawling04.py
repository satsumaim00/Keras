from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "sj6IFFPTvDc6xIf6Z8WTNftwtXOiQjkW7F3BMDI6DTMwoNCk%2FZJ3ANETMv29xBYKkt7y3EZpX1%2FNMhdJkXE7dQ%3D%3D"

Q0 = quote("서울특별시")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "5000"


paramset = "serviceKey=" + serviceKey + "&Q0=" + Q0 + "&Q1=" + "&ORD=" +ORD + "&pageNo=" + pageNo + \
           "&startPage=" + startPage + "&numOfRows=" + numOfRows

url = endpoint + paramset
print("url : " +url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")



for item in items:
    tagged_item = item.find("dutyname")
    print(tagged_item.text)

count=0
for item in items:
    tagged_item = item.find("dutytime1c")
    if(tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            count += 1

print("서울특별시 내 월요일 9시 이후까지 하는 약국의 개수 : " + str(count))