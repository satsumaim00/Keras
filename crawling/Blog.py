import urllib.request
import bs4
import os
from selenium import webdriver
import re
driver = webdriver.Chrome(os.path.abspath('chromedriver'))
driver.get('https://blog.naver.com/skcmi/221436159512/')
driver.switch_to.frame('mainFrame')
html = driver.page_source
# print(html)




bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("div", {"class":"se-main-container"})

lis= str(ul.findAll("p"))
lis2= str(ul.findAll("img"))
lis = re.sub('<.+?>', '', lis, 0).strip()
print(lis)

# print(lis2)
print("이미지 및 이모티콘 개수 :",lis2.count("img"),"개")


driver.close()

