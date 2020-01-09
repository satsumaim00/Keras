# 아이돌, 날짜, 네이버 뉴스 추출해서 엑셀파일 저장
import pandas as pd
from sqlalchemy import create_engine
import urllib.request
import bs4
from urllib import parse
import pymysql
import psycopg2
import csv
con = pymysql.connect(host = "localhost", user = "root", password ="1234",
                      db = "idol_rank")

cur = con.cursor()

data_sql = "select idol, 날짜 from idol_rank.idol_chart"
cur.execute(data_sql)
datas = cur.fetchall()
name_l = []
date_l = []

for data in datas:
    # print(data)
    name = data[0]
    name_l.append(name)
    date = data[1]
    date_l.append(date)

nrow_sql = "SELECT COUNT(*) FROM idol_chart;"
cur.execute(nrow_sql)
nrow = cur.fetchone()[0]


print(nrow)
list = []
count = 0

for i in range(0, nrow, 1):
    # query = {'query' : name_l[i]}
    # name_url = parse.urlencode(query, encoding='UTF-8', doseq=True)
    name_url = urllib.parse.quote_plus(name_l[i])

    url = 'https://search.naver.com/search.naver?where=news&query=' + name_url + '&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=' \
          + str(date_l[i])[:4] + "." + str(date_l[i])[4:] + '.01&de=' + str(date_l[i])[:4] + "." + str(date_l[i])[4:] \
          + '.31&docid=&nso=so%3Ar%2Cp%3Afrom' + str(date_l[i]) + '01to' + str(date_l[i]) + '31%2Ca%3Aall&mynews=0&refresh_start=0&related=0'


    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "lxml")

    ul = bs_obj.find("div", {"class":"title_desc all_my"})
    try:
        lis= ul.find("span")
        span = lis.text.split('/')
        wws = span[1]
        wws = wws.replace("건", "").replace(",", "").replace(" ", "")
        result = wws, name_l[i], date_l[i]
        list.append(result)
        print(list)
    except:
        except_result = '0', name_l[i], date_l[i]
        list.append(except_result)
        print(list)
        pass
#
#
# print(list)



# lists = [('5998', '방탄소년단', 201801), ('647', 'TWICE', 201801), ('605', 'WannaOne', 201801), ('4637', '레드벨벳', 201801), ('3063', '아이유', 201801), ('1961', '볼빨간사춘기', 201801), ('902', 'EXO', 201801), ('60', 'BLACKPINK', 201801), ('4995', '선미', 201801), ('1721', '종현', 201801)]

# print(lists)
f = open('excelD.csv', 'w', newline='', encoding='euc_kr')
wr = csv.writer(f)
for li in list:
    wr.writerow(li)
f.close()


# list1 = []
# f = open('excel.csv', 'r')
# rdr = csv.reader(f)
#
# for line in rdr:
#
#     list1.append(tuple(line))
# f.close()
# print(list1)


# print(list)
# df = pd.DataFrame(list, columns=['Naver_News'])
# df_c = pd.concat([data, df], axis=1)
#
# df_c.to_excel('test_multi.xlsx', sheet_name = 'sheet1')
# # df_c.to_sql(name='idol_chart', con=engine, if_exists='replace', index = False)
# display(df_c)


#
# make_sql = "ALTER TABLE idol_chart ADD(Naver_News TEXT);"
# cur.execute(make_sql)
# con.commit()
#
# insert_sql = "INSERT INTO idol_chart(Naver_News) values " +str(list)
# cur.execute(insert_sql)
# con.commit()
#
# con.close()
