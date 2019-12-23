import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"
result = requests.get(url , headers=headers)

bs_obj = bs4.BeautifulSoup(result.text)

ul = bs_obj.find("ul", {"class":"prdList grid4"})

boxes = ul.findAll("div", {"class":"box"})

# def get_product_info(box):
#     ptag = box.find("p", {"class": "name"})
#     spans_name = ptag.findAll("span")
#     ul = box.find("ul")
#     spans_price = ul.findAll("span")

def get_product_info(box):
    ptag = box.find("p", {"class": "name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    atag = box.find("a")
    link = atag['href']
    name = spans_name[0].text
    price = spans_price[1].text

    return {"name":name, "price":price, "link":link}

for box in boxes:
    product_info = get_product_info(box)
    print(product_info)
