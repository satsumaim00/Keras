from urllib.request import urlopen
import json

from_date = "2019-01-01"
to_date = "2019-12-23"
url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/"+ from_date + "/edate/" + to_date
text = urlopen(url)
json_objs = json.load(text)

print(json_objs)

