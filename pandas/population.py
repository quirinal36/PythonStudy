import pandas as pd

df = pd.read_excel('population.xlsx', header=2, usecols='B,C,D,E,F')
print(df)

# 연도별로 인구가 가장 많았던 동네를 
# 완산구, 덕진구 에서 골라 화면에 표시하자