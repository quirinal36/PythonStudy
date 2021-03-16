import urllib.request
import ssl
import json

query = input('검색어를 입력 해주세요: ')

with open('naver_secret.json', 'r') as api_key:
    client_info = json.load(api_key)

url = 'https://openapi.naver.com/v1/search/errata.json'

encText = '?query={}'.format(urllib.parse.quote(query))

url = url + encText
print(url)

request = urllib.request.Request(url)
request.add_header('X-Naver-Client-Id', client_info.get('client_id'))
request.add_header('X-Naver-Client-Secret', client_info.get('client_secret'))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(request, context=ctx)

content = response.read().decode('UTF-8')

print(content)