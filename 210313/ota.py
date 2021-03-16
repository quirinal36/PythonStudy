"""
1. 검색어 입력받기
2. URL 만들기 (검색어를 뒤에 붙여서)
3. urllib 활용해 요청(request)
4. 응답(response)받은 자료를 JSON 형태로 변환
5. 변환한 자료를 터미널 창에 띄우기
"""

search = input('검색어를 입력 해주세요: ')

with open('naver_secret.json', 'r') as json_file:
    api_key = json.load(json_file)

print(api_key)