import time
from selenium.webdriver import Chrome
import pandas as pd

webdriver = "C:\PythonProjects\chromedriver.exe"

driver = Chrome(webdriver)

# url = "https://www.idol-chart.com/"



for i in range(1, 13):
    for j in range(1, 6):
        u = "https://www.idol-chart.com/ranking/month/?sm=2018" + str(i).rjust(2, "0") + "&page=" + str(j)

        driver.get(u)
        time.sleep(3)
        # items = driver.find_elements_by_class_name("section")
        items = driver.find_elements_by_class_name("layout-bbs")

        for li in items:
            print(li.text)

driver.close()


