from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import json

class InstaInfo:
    def __init__(self) :
        self.username = ''
        self.timeinfo = ''
        self.likes = ''


    def  __str__(self) :
        return 'username: {}, timeinfo: {}, likes: {}'.format(self.username, self.timeinfo, self.likes)



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


for i in range(100):
    if not driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow'):
        break

    info = InstaInfo()
    # 1. username 정보 
    try:
        info_username = driver.find_element_by_css_selector('.sqdOP.yWX7d._8A5w5.ZIAjV').text
        info.username = info_username
    except:
        info_username = ''
    # 2. 시간정보 수집
    time_raw = driver.find_element_by_css_selector('time.FH9sR.Nzb55')
    time_info = time_raw.get_attribute('datetime')
    info.timeinfo = time_info
    # 3. 좋아요 갯수 수집
    try:
        like = driver.find_element_by_css_selector('.zV_Nj span').text
        info.likes = like
    except:
        like = ''
    

    print(info)

    driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
    time.sleep(1.5)
