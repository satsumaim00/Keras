import requests
from urllib.parse import urlparse

keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" +keyword + "&display=100"
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"0nDzzu36nMXk9_jmGkyE",
                                "X-Naver-Client-Secret":"Mo22YFZZw6"})
json_obj = result.json()
print("display : " + str(json_obj['display']))
print("start : " + str(json_obj['start']))
print("items : " + str(len(json_obj['items'])))
print(json_obj)