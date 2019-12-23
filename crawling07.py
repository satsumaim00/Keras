import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"

result = requests.get(url, headers=headers)

bs_obj = BeautifulSoup(result.text)

profile_name = bs_obj.find("p", {"class":"name"})

h1_bp_name = profile_name.find("span")
bp_name = h1_bp_name.text
print(bp_name)

profile_name1 = bs_obj.find("ul", {"class":"xans-element- xans-product xans-product-listitem"})

h1_bp_name1 = profile_name1.find("li")
bp_name1 = h1_bp_name1.text
print(bp_name1)

