import xml.etree.ElementTree as ET
from urllib import request, error, parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter a url: ")
data = request.urlopen(url, context=ctx).read().decode()
summation = 0

tree = ET.fromstring(data)
counts = tree.findall('.//count')

for count in counts:
    summation += int(count.text)

print(summation)
