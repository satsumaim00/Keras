import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("ul", {"class":"an_l"})
first_a = top_right.find("a")


print(top_right.text)


