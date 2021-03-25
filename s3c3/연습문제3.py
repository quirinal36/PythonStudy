import random

print('☆ 구구단 테스트')
num1 = random.randint(2,9)
num2 = random.randint(1,9)

답변 = int(input('{} x {} ='.format(num1, num2)))
정답 = num1 * num2
if 답변 == 정답:
    print('맞았습니다.')
else :
    print('틀렸습니다.')