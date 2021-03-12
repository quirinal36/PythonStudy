from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import json
import urllib.request

with open('./insta_id.json', 'r') as api_key:
    client_info = json.load(api_key)

driver = webdriver.Chrome('chromedriver')

driver.get('https://instagram.com')

"""
driver.find_element_by_css_selector('.class명')
driver.find_element_by_css_selector('#id명')
driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
"""

driver.implicitly_wait(5)

#아이디 입력
inputName = driver.find_element_by_css_selector("input[name='username']")
inputName.send_keys(client_info.get('id'))
#비밀번호 입력
inputPwd = driver.find_element_by_css_selector("input[name='password']")
inputPwd.send_keys(client_info.get('pwd'))
#로그인 버튼 누르기
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
# 요소가 안보이면 알아서 기다려라
driver.implicitly_wait(5)

#로그인 정보를 저장하시겠습니까? 창 넘어가기
save_login_info_button= driver.find_element_by_xpath("//button[text()='나중에 하기']")
save_login_info_button.click()
driver.implicitly_wait(5)
#로그인 정보를 저장하시겠습니까? 창 넘어가기
notification_button= driver.find_element_by_xpath("//button[text()='나중에 하기']")
notification_button.click()
driver.implicitly_wait(5)

# 태그 검색 페이지 이동
driver.get('https://instagram.com/explore/tags/bts/')
# 첫째사진 누르기
first_post = driver.find_element_by_class_name('eLAPa')
first_post.click()
#사진저장, 다음 반복

1. 