from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from selenium.common.exceptions import NoSuchElementException 
from dotenv import load_dotenv
import os

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.file_url);
        """)

# 환경 변수 로드
load_dotenv()

USER_ID = os.getenv("USER_ID")
USER_PWD = os.getenv("USER_PASSWORD")

# driver = webdriver.Remote(
#     command_executor='http://192.168.99.100:8910',
#     desired_capabilities=DesiredCapabilities.PHANTOMJS)

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')

options.add_experimental_option("prefs", {
  "download.default_directory": r"d:\kidsnot\downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome('../chromedriver', options=options)

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

## 배열이 되어야 한다.

print('4. 리스트 중 처음 껄로 선택')
contents = driver.find_element_by_class_name("album-list-wrapper")
# firstListItem = driver.find_element_by_xpath("//a[contains(@href,'req=/albums/')]")

## 배열이 되어야 한다.
items = contents.find_elements_by_tag_name("a")
# items[0].click()
album_idx = 1
for item in items:
    # print(idx + ' 번째 실행')
    alubm_item = driver.find_element_by_xpath("//div[@class='album-list-wrapper']//a["+str(album_idx)+"]")
    driver.execute_script("arguments[0].click();", alubm_item)
    driver.save_screenshot("kidsnote_imgs/4_kids_note_click_item.png")

    driver.implicitly_wait(3)
        
    if check_exists_by_xpath("//div[@class='role-name-select-wrapper']"):
        print('5. 호칭 선택')        
        nicknames_form = driver.find_element_by_xpath('//div[@class="role-name-select-wrapper"]//div//div[1]/form[1]')
        nicknames_form.submit()
        driver.save_screenshot("kidsnote_imgs/5_kids_note_click_nick_name_selector.png")

    # 비디오 다운로드    
    if check_exists_by_xpath("//div[@class='download-button-wrapper']"):    
        print('6. 비디오 다운로드')
        video_a = driver.find_element_by_xpath("//div[@class='download-button-wrapper']//a")
        print(video_a.get_attribute('innerHTML'))
        video_a.click()
        paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
        driver.back()

    img_grid_container = driver.find_element_by_id("img-grid-container")
    if img_grid_container:
        print('7. 모든 이미지 다운로드')
        img_a_tags = driver.find_elements_by_xpath('//div[@id="img-grid-container"]//div[@class="grid"]')
        idx = 1
        for img_a_tag in img_a_tags:
            driver.find_element_by_xpath('//div[@id="img-grid-container"]//div['+str(idx)+']//a').click()
            org_img_tag=driver.find_element_by_xpath("//a[contains(text(),'원본')]")
            org_img_tag.click()
            WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
            idx += 1
            driver.back()      
                  
    driver.implicitly_wait(10)            
    driver.back()
    if album_idx <= 1:
        driver.back()
    album_idx += 1



driver.quit()

#get_attribute('innerHTML')