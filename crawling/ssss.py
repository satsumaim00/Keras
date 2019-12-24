from urllib import parse
import urllib.request
import bs4
query = { 'query' : '아이유' }
ss=parse.urlencode(query, encoding='UTF-8', doseq=True)

# print(ss)
# url = 'https://search.naver.com/search.naver?where=news&'+ ss +'&sm=tab_opt&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2018.01.01&de=2018.01.31&docid=&nso=so%3Add%2Cp%3Afrom20180101to20180131%2Ca%3Aall&mynews=0&refresh_start=0&related=0'

for i in range(1, 13):
    url = 'https://search.naver.com/search.naver?where=news&'+ ss +'&sm=tab_opt&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2018.' + str(i).rjust(2, "0") + '.01&de=2018.' + str(i).rjust(2,"0") + '.31&docid=&nso=so%3Add%2Cp%3Afrom20180101to20180131%2Ca%3Aall&mynews=0&refresh_start=0&related=0'



    print(url)





