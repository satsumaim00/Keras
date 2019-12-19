from urllib.request import urlopen

url = "http://www.naver.com"
html = urlopen(url)

print(html.read())
