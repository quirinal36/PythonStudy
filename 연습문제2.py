x = int(input('X좌표를 입력 해주세요 : '))
y = int(input('Y좌표를 입력 해주세요 : '))

사분면 = 0 
if y > 0:
    if x > 0:
        사분면 = 1
    else: 
        사분면 = 2
else:
    if x < 0:
        사분면 = 3
    else: 
        사분면 = 4    

print('({}, {})는 {} 사분면에 위치해 있습니다.'.format(x, y, 사분면))