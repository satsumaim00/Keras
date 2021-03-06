import bs4
from selenium import webdriver
import os
import urllib.request
import re

options = webdriver.ChromeOptions()
options.add_argument('headless') # 팝업창 안띄우는 속성
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get('https://blog.naver.com/skcmi/221436159512/')
driver.implicitly_wait(3)
driver.switch_to.frame('mainFrame')
html = driver.page_source
# print(html)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("div", {"class":"se-main-container"}) # 본문 영역 가져오기

# lis= str(ul.findAll("p"))
lis= ul.findAll("p") # 문장이 있는 p 태그 추출
lis2 = ul.findAll("img", {"class": "se-sticker-image"}) #이모티콘 추출
image = ul.findAll("img", {"class": "se-image-resource"}) #이미지 추출
canvas = ul.findAll("div", {"class": "se-component se-video se-l-default"}) # 동영상 추출

# lis = re.sub('<.+?>', '', lis, 0).strip()
# content = list(lis)
list = [] #문자를 넣어주기 위한 리스트

for li in lis:  # \u200b 제거후 텍스트 추출
    if li.text != '\u200b':
        list.append(li.text) #빈 리스트에 li의 텍스트를 반복문으로 이어 붙이기



for li2 in lis2: #이모티콘 개수
    str(lis2).count("img")

for li3 in image: #이미지 개수
    # print(li3)
    str(image).count("img")

for li4 in canvas: #동영상 개수
    str(canvas).count("se-component se-video se-l-default")

print("이모티콘 개수 : ",str(lis2).count("img"),"개")
print("이미지 개수 : ",str(image).count("img"),"개")
print("동영상 개수 : ",str(canvas).count("se-component se-video se-l-default"),"개")
print(list)




