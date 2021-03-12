import json

api_key = {
    'client_id' : 'BNidahojeq2_rJKwP41X',
    'client_secret' : 'gZ5_wDOEIB'
}

# 딕셔너리 생성, 읽기, 수정 하는 방법
# 0. 생성
# api_key = {}
# 1. 읽기
# print( api_key['client_id'] )
# 2. 삽입
api_key['name']='leehg'
#print(api_key)
# 3. 수정
api_key['name']='이형구'
#print(api_key)
# 4. 반복문으로 전체 값 읽기
for key in api_key.keys():
    print(key)
print("____________")
for value in api_key.values():
    print(value)
print("____________")
for key, value in api_key.items():
    print(key, value)


print(api_key.get('name')) # api_key['name']

with open('naver_secret.json', 'w') as json_file:
    json.dump(api_key, json_file)