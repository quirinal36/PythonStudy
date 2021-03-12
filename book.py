from booksearch import search, dsearch
import json

"""
sim: 유사도순
date: 출간일순
count: 판매량순
"""
sort = ['sim','date', 'count']
# 검색 시작위치, 최대 1000까지 가능
start = 1
# 검색 결과 출력 건수 지정 (기본: 10, 최대: 100)
display = 30
# 검색어
query = 'python'

result = dsearch(query, display, start, sort[2])
books = result.get('items')
print(len(books))
for book in books:    
    print(book.get('title'))

bookinfo = {}
bookinfo['books'] = books

with open('search_result.json', 'w', encoding='UTF-8') as json_file:
    json_file.write(json.dumps(bookinfo, ensure_ascii=False, indent=2))