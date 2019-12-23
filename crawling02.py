import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-cafe-calgary/"

result = requests.get(url=url)
bs_obj = BeautifulSoup(result.content, "html.parser")

profile_name = bs_obj.find("div", {"class":"profile-name"})

h1_bp_name = profile_name.find("h1")
bp_name = h1_bp_name.text
print(bp_name)


profile_name1 = bs_obj.find("div", {"class":"buttons medium button-plain"})
h1_bp_name1 = profile_name1.find("span")
bp_name1 = h1_bp_name1.text
print(bp_name1)
