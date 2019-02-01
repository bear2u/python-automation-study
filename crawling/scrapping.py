import requests
from bs4 import BeautifulSoup

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
print(response.status_code)

# 페이지 파싱
page = BeautifulSoup(response.text, 'html.parser')

# 페이지 제목 얻기
print(page.title)
print(page.title.string)

# h3 페이지의 모든 요소를 찾는다
print(page.find_all('h3'))

