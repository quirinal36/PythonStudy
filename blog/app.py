from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import pyperclip

# 로그인 정보 가져오기
with open('./insta/naver_login.json', 'r') as login_info:
    login = json.load(login_info)

browser = webdriver.Chrome('./insta/chromedriver')
browser.get('https://nid.naver.com/nidlogin.login?svctype=262144&amp;url=http://m.naver.com/aside/')

time.sleep(2)
input_id = browser.find_element_by_css_selector('#id')
# 복사하기
pyperclip.copy(login.get('id'))
# 붙여넣기
input_id.send_keys(Keys.CONTROL, 'v')

input_pw = browser.find_element_by_css_selector('#pw')
# 복사하기
pyperclip.copy(login.get('pwd'))
# 붙여넣기
input_pw.send_keys(Keys.CONTROL, 'v')

# 로그인 버튼 누르기
login_btn = browser.find_element_by_id('log.login')
login_btn.click()

# 글작성 페이지로 이동하기
time.sleep(3)
browser.get('http://m.blog.naver.com/turboguy')
time.sleep(2)
browser.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FPostList.nhn%3Fpermalink%3Dpermalink%26blogId%3Dturboguy&targetCategory=67')
time.sleep(1.5)

# 제목 작성하기
title_text = browser.find_element_by_css_selector('.documentTitle_blog .se_textarea')
title_text.send_keys('제목입니다.')

# 본문 작성하기
content_text = browser.find_element_by_css_selector('.se_sectionArea .se_textarea')
content_text.send_keys('본문입니다.')