import pandas as pd

# DataFrame
df = pd.read_csv('pandas/credit.csv')

# 1
# 세로 줄 출력 df[컬럼명]
# 딕셔너리와 비슷하다
df['나이']

# 2
# 평균 구하기
df['나이'].mean()

# 3
# 최빈값 : 가장많이 관측되는 수(또는 문자열)
df['학력'].mode()

# 4
# 최대값
df['사용금액'].max()

# 5
# 최소값
df['사용금액'].min()

# 6
# describe : [count, mean, std, min, 25%, 50%, 75%, max] 출력
# 컬럼 두개를 동시에 출력하고 싶다.
df[ ['사용금액', '사용횟수'] ].describe()

# 7
# groupby
# M 의 평균과 F 의 평균을 구분하여 보고싶다.
print(df[ ['성별', '사용금액'] ].groupby('성별').mean())