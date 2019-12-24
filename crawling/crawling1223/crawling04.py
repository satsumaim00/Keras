import requests
from urllib.parse import urlparse

keyword = "광운대"
url = "https://openapi.naver.com/v1/search/blog?query=" +keyword
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"0nDzzu36nMXk9_jmGkyE",
                                "X-Naver-Client-Secret":"Mo22YFZZw6"})
json_obj = result.json()
for item in json_obj['items']:
    print("Title : " + item['title'].replace("<b>","").replace("</b>",""),
            "Link : " + item['link'])   #b태그 없애는 속성