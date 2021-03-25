score = int(input('점수를 입력하세요:'))

print('{}점 입니다.'.format(score))

grade = 5
if score >= 90:
    grade = 1
elif score >= 80:
    grade = 2

print('{}등급이군요 ^^'.format(grade))
