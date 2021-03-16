import pandas as pd

df = pd.read_csv('pandas/credit.csv')

df.groupby('성별').mean()

# 1. correlation
# 1과 가까워질수록 연관성이 크다는 뜻
# print(df[['나이', '사용금액']].corr())

# 2. 조건식을 활용
# 나이 40 초과 
# 190개 자료 선택됨
# print(df[ df['나이'] > 40 ])

# 3. query 활용
# 나이 50초과, 결혼상태 'Married'인 데이터
# 65개 자료 선택됨
df.query("나이 > 50 and 기혼 == 'Married'")


# 4. 리스트 데이터를 dataframe 으로 변환
shirts = [15, 20, 25]
pants = [150, 160, 170]

clothes = {
    '셔츠' : shirts,
    '바지' : pants
}

data = pd.DataFrame(clothes)

# 5. 파일 내보내기
# data.to_csv('clothes.csv')

# 6. 한글 깨짐 복구
data.to_csv('clothes.csv', encoding='UTF-8-SIG')

# 7. 
# 결혼한 남자('기혼'=='Married', '성별'=='M')가 
# 결혼하지 않은 남자('기혼'=='Single', '성별'=='M') 보다
# 사용금액이 평균적으로 높은가?
# print(df.query("기혼=='Married' and 성별=='M'").mean())
# print(df.query("기혼=='Single' and 성별=='M'").mean())

# 8.
# 소득이 높을수록 사용금액이 평균적으로 높은가?
# groupby('소득') 을 활용
print(df[['소득', '사용금액']].groupby('소득').mean())