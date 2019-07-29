from urllib import request, error, parse
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter a url: ")
js = request.urlopen(url, context=ctx).read().decode()
summation = 0

data = json.loads(js)

lst = data['comments']
for item in lst:
    summation += int(item["count"])

print(summation)
