"""
print('★ 선물하기 ★', end='\n')
gift = input('선물을 입력하세요 :')
numA = int(input('가로길이를 입력하세요 :'))
numB = int(input('세로길이를 입력하세요 :'))
numC = int(input('높이를 입력하세요 :'))

# 겉넓이 구하기
result1 = ???
# 부피 구하기
result2 = ???

print(gift + '의 겉넓이는 '+ str(result1) + '입니다.')
print('%s의 부피는 %d 입니다.' %(gift, result2))
"""
numD = 3.3456789
print("실수를 출력 %f (good)" %numD)

print("소수점 두번째 자리까지 출력 %.2f (good)" %numD)

numD = round(numD, 2)
print("실수를 출력 %f (good)" %numD)