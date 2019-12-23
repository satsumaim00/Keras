import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"

result = requests.get(url , headers=headers)

bs_obj = BeautifulSoup(result.text)
print(bs_obj)