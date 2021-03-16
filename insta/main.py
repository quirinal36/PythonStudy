import pandas as pd
from app import search 

result = search()

data = pd.DataFrame(
    [ (i.username, i.timeinfo, i.likes) for i in result ], 
    columns=['아이디', '날짜', '좋아요']
    )
print(data)
data.to_excel('export.xlsx')