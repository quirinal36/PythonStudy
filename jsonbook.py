import json
import requests
import pandas as pd

class BookInfo:
    def __init__(self):
        self.title = ''
        self.link = ''
        self.image = ''
        self.author = ''
        self.price = ''
        self.discount = ''
        self.publisher = ''
        self.pubdate = ''
        
    def __str__(self):
        return 'title:{}\nlink:{}'.format(self.title, self.link)

url = 'https://elasticbeanstalk-ap-northeast-2-273466070173.s3.ap-northeast-2.amazonaws.com/search_result.json'
req = requests.get(url)
data = req.json()

books = data.get('books')

li = list()

for book in books:
    info = BookInfo()

    info.title = book.get('title')
    info.link = book.get('link')
    info.image = book.get('image')
    info.author = book.get('author')
    info.price = book.get('price')
    info.discount = book.get('discount')
    info.publisher = book.get('publisher')
    info.pubdate = book.get('pubdate')
    
    li.append(info)


df = pd.DataFrame(
    [(info.title, info.price) for info in li],
    columns = ['제목', '정가']
)
#s = Series(data=data, index=index)
 
df.to_excel("books.xlsx", encoding='UTF-8-SIG')

# 평균 가격
# 가장 높은가격
# 가장 낮은가격
print(df['정가'].mean())
print(df['정가'].min())
print(df['정가'].max())