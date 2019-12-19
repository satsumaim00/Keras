import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

li = bs_obj.find("li")
ul = bs_obj.find("ul")

print(li.text)
print(li)
print(ul)