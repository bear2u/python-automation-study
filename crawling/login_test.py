import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# 아이디와 비밀번호 지정

USER_ID = os.getenv("USER_ID")
USER_PWD = os.getenv("USER_PASSWORD")

# 세션 시작하기
session = requests.session()

# 로그인하기
login_info = {
    "m_id": USER_ID,
    "m_passwd": USER_PWD
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
# 오류 발생시 예외가 발생한다
res.raise_for_status()

# 마이페이지 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)