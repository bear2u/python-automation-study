from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

USER_ID = os.getenv("USER_ID")
USER_PWD = os.getenv("USER_PASSWORD")

driver = webdriver.Remote(
    command_executor='http://192.168.99.100:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

driver.implicitly_wait(3)

url_login = 'https://www.kidsnote.com/login/'
driver.get(url_login)
print('1 로그인 페이지에 접속합니다');

driver.save_screenshot("kidsnote_imgs/1_kids_note_login.png")

e = driver.find_element_by_id('id_username')
e.clear()
e.send_keys(USER_ID)

e = driver.find_element_by_id('id_password')
e.clear()
e.send_keys(USER_PWD)

# 로그인
form = driver.find_element_by_css_selector("input.btn[type=submit]")
form.submit()
print('2. 로그인 버튼 클릭');
driver.save_screenshot("kidsnote_imgs/2_kids_note_login_done.png")

# driver.find_element_by_css_selector('a[href="http://www.iana.org/domains/example"]').click()

# 앨범 클릭
albumClick = driver.find_element_by_xpath("//a[@href='/albums/']")
albumClick.click()
print('3. 앨범을 클릭');
driver.save_screenshot("kidsnote_imgs/3_kids_note_click_album.png")

print('4. 리스트 중 처음 껄로 선택')
contents = driver.find_element_by_class_name("content")
# firstListItem = driver.find_element_by_xpath("//a[contains(@href,'req=/albums/')]")

items = contents.find_elements_by_tag_name("a")
items[0].click()
driver.save_screenshot("kidsnote_imgs/4_kids_note_click_first_item.png")

driver.implicitly_wait(3)

print('5. 호칭 선택')
nicknames = driver.find_elements_by_class_name("form-select-nickname")
nicknames_form = nicknames[10].find_element_by_tag_name("form")
nicknames_form.submit()
driver.save_screenshot("kidsnote_imgs/5_kids_note_click_nick_name_selector.png")

# 비디오 다운로드
video_div = driver.find_element_by_class_name('download-button-wrapper')
if video_div:    
    print('6. 비디오 다운로드');
    video_button.click()


driver.quit()