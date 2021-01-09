print('★ 생일 선물 ★', end='\n\n')
gift = input('선물을 입력하세요. :')
horizon = int(input('가로의 길이(cm)는? '))
vertical = int(input('세로의 길이(cm)는? '))
height = int(input('높이(cm)는? '))
surface = str(2*(horizon*vertical + horizon * height + vertical * height)) + '㎤'
volume = str(horizon * vertical * height)+'㎤'

print(gift, '선물 상자의 겉넓이 :', surface)
print(gift, '선물 상자의 부피 :', volume)

