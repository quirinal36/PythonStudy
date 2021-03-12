import urllib.request
import ssl
import json

with open('naver_secret.json', 'r') as json_file:
    api_key = json.load(json_file)

# keyword = input('검색하고 싶은 책을 입력하세요:')

url = 'https://elasticbeanstalk-ap-northeast-2-273466070173.s3.ap-northeast-2.amazonaws.com/search_result.json'
print(url)

request = urllib.request.Request(url)
"""
request.add_header('X-Naver-Client-Id', api_key.get('client_id'))
request.add_header('X-Naver-Client-Secret', api_key.get('client_secret'))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
"""
response = urllib.request.urlopen(request)

print(response.getcode())
print(response.read().decode('UTF-8')) # 인코딩 되어있는 정보

content = response.read().decode('UTF-8')

json_result = json.loads(content)
books = json_result.get('books')
print('books 의 길이: ', len(books))
book1 = books[0]
print('제목: ', book1.get('title'))
print('Link: ', book1.get('link'))
print('Image: ', book1.get('image'))