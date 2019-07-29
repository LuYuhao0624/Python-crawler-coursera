from bs4 import BeautifulSoup as bs
from urllib import request, error, parse
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter a url: ")

iter = eval(input('enter count: '))

for i in range(iter):
    html = request.urlopen(url, context=ctx).read()
    soup = bs(html, 'html.parser')
    tags = soup('a')
    url = tags[17].get('href', None)

print(re.findall('([A-Za-z]+)\.html', url))
