import requests
from urllib.parse import  urlparse

keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword
result = requests.get(urlparse(url).geturl(),
            headers={"X-Naver-Client-id":"0nDzzu36nMXk9_jmGkyE",
                        "X-Naver-Client-Secret":"Mo22YFZZw6"})
json_obj = result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])
