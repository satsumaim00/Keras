import requests
from urllib.parse import urlparse

def get_api_result(keyword, display,start):
    url =  "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display" + str(display) +"&start=" \
           + str(start)

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"0nDzzu36nMXk9_jmGkyE",
                                    "X-Naver-Client-Secret":"Mo22YFZZw6"})
    return result.json()

json_obj = get_api_result("광운대", 100, 101)

for item in json_obj['items']:
    print(item)

# print("display:", json_obj['display'])
# print("start:", json_obj['start'])
# print("items:", json_obj['items'])