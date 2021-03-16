from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
import pyperclip
import json

with open('./insta/naver_login.json', 'r') as login_info:
    login = json.load(login_info)

옵션 = webdriver.ChromeOptions()
옵션.add_argument('user-data-dir=C:/Users/turbo/AppData/Local/Google/Chrome/User Data/Default')

browser = webdriver.Chrome('./insta/chromedriver', chrome_options=옵션)
browser.get('https://nid.naver.com/nidlogin.login?svctype=262144')

time.sleep(3)

input1 = browser.find_element_by_css_selector('#id')
pyperclip.copy(login.get('id'))
input1.send_keys(Keys.CONTROL, 'v')

input2 = browser.find_element_by_css_selector('#pw')
pyperclip.copy(login.get('pwd'))
input2.send_keys(Keys.CONTROL, 'v')

login_btn = browser.find_element_by_id('log.login')
login_btn.click()

time.sleep(2)

browser.get('https://m.blog.naver.com/'+login.get('id'))
time.sleep(2)
browser.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2Fturboguy%3FRedirect%3DWrite&targetCategory=43')
time.sleep(2)

title_area = browser.find_element_by_css_selector(".documentTitle_blog .se_textarea")
title_area.send_keys('TEST')

contents = browser.find_element_by_css_selector(".se_sectionArea .se_editable")
contents.send_keys('본문')

postBtn = browser.find_element_by_css_selector(".btn_applyPost") # 등록 버튼
postBtn.click()
# 발행완료