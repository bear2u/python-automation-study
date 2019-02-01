from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://192.168.99.100:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

driver.get('https://www.kidsnote.com/login/')
driver.save_screenshot("kids_note.png")
# driver.find_element_by_css_selector('a[href="http://www.iana.org/domains/example"]').click()

driver.quit()