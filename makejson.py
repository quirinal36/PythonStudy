import json

naverApi = {
    "client_id" : "BNidahojeq2_rJKwP41X",
    "client_secret" : "gZ5_wDOEIB"
}

with open('naver_secret.json', 'w') as json_file:
    json.dump(naverApi, json_file)
