import urllib.request
import ssl
import json

client_id = 'BNidahojeq2_rJKwP41X'
client_secret = 'gZ5_wDOEIB'

url = 'https://openapi.naver.com/v1/search/book.json'


encText = "?query="+ urllib.parse.quote('python')
url = url + encText
print(url)

request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(request, context=ctx)
print(response.getcode())

content = response.read().decode('UTF-8')
searchResult = json.loads(content)
items = searchResult.get('items')

for item in items:
    print(item.get('title'))