import requests
from urllib.parse import urlparse

def get_api_result(keyword, display,start):
    url =  "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display" + str(display) +"&start=" \
           + str(start)

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"0nDzzu36nMXk9_jmGkyE",
                                    "X-Naver-Client-Secret":"Mo22YFZZw6"})
    return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 500, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>","").replace("</b>","")
        print(title + "@"+item['bloggername'] + "@" + item['link'])

keyword = "광운대학교"

call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)