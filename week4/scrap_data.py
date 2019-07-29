from bs4 import BeautifulSoup as bs
from urllib import request, error, parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter a url: ")
html = request.urlopen(url, context=ctx).read()
soup = bs(html, 'html.parser')
summation = 0

tags = soup('span')
for tag in tags:
    summation += int(tag.contents[0])

print(summation)
