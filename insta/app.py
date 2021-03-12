from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import json

with open('insta_id.json', 'r') as api_key:
    client_info = json.load(api_key)

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://instagram.com')

"""
driver.find_element_by_css_selector('.class명')
driver.find_element_by_css_selector('#id명')
driver.find_element_by_css_selector('태그명[속성이름="속성명"]')
"""

driver.implicitly_wait(5)

inputName = driver.find_element_by_css_selector("input[name='username']")
inputName.send_keys(client_info.get('id'))
inputPwd = driver.find_element_by_css_selector("input[name='password']")
inputPwd.send_keys(client_info.get('pwd'))
inputPwd.send_keys(Keys.ENTER)

driver.find_element_by_css_selector('button[class="sqdOP"]').click()
driver.implicitly_wait(5)
# 페이지 이동

# 요소가 안보이면 알아서 기다려라
# 첫째사진 누르기

#사진저장, 다음 반복

image = driver.find_element_by_css_selector('.FFVAD').get_attribute('src')
filename = image.substring(image.rfind('/'), image.find('.jpg'))
print(filename)
#urllib.request.urlretrieve(image, './download')