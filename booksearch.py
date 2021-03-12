import urllib.request
import ssl
import json

def search(query):
    ddisplay = 10
    dstart = 1
    dsort = 'sim'
    return dsearch(query, ddisplay, dstart, dsort)

    
def dsearch(query, display, start, sort):
    with open('naver_secret.json', 'r') as api_key:
        client_info = json.load(api_key)

    url = 'https://openapi.naver.com/v1/search/book.json'

    encText = "?query={}&display={}&start={}&sort={}".format(urllib.parse.quote(query), display, start, sort)
    url = url + encText
    print(url)

    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_info.get('client_id'))
    request.add_header('X-Naver-Client-Secret', client_info.get('client_secret'))

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    response = urllib.request.urlopen(request, context=ctx)
    print(response.getcode())

    content = response.read().decode('UTF-8')
    searchResult = json.loads(content)

    return searchResult