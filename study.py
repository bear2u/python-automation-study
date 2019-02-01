from selenium import webdriver #selenium을 이용해 크롬에서 파싱홤.

def list_print(num:int) :
    article_name = driver.find_elements_by_css_selector('div.board-name > div.inner_name > a') #div태그 class값이 board-name의 자식노드 div 태그 class값이  inner_name이면서 갖을 때 태그a를 갖고 있다면 가져옴" 
    print(article_name[num].text)
    article_list = driver.find_elements_by_css_selector('div:not(#upperArticleList) > table > tbody > tr > td > div.board-list > div.inner_list > a') #div:not(#upperArticleList)은 갖고 있지 않는 것만 가져감.
    print(article_list[num].text)
    print(article_list[num].get_attribute("href"))

if(__name__=="__main__"):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1920')
    options.add_argument("--disable-gpu")
    #chromedriver를 미리 받아놓고 headless(창 없이 뛰운다) 실행한다.
    driver = webdriver.Chrome("./chromedriver", options=options) 
    
    driver.implicitly_wait(3) #브라우저의 정상적인 기동을 위해 3초를 기다린다.
    driver.get("https://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&amp;search.boardtype=L&amp;viewType=pc") #중고카페 전체리스트를 가져오는 주소
    
    driver.switch_to.frame('cafe_main') # cafe_main 프레임으로 전환한다.

    driver.get_screenshot_as_file('naver_main_headless.png')#비교하기 위해 저장함.

    for n in range(10): # 10개의 정도 돌림
        list_print(n)   # 파싱해서 찍음

    driver.quit() #크롬을 종료한다.
