

'''
- 네이버로 접속해서 뉴스스탠드 쪽 파란 '네이버뉴스' 클릭 -> 

정치, 경제, 사회, 생활/문화, 세계, IT/과학 탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭해 주시면 됩니다,
뒤로가기는 driver.back() 메서드로 뒤로가기 가능.

XPATH를 따다보면 규칙을 발견할 수 있을겁니다.
반복분 이용해서 클릭 명령을 내려주시면 됩니다.
24개의 명령 일일이 쓰기 X, 규칙을 찾아보세요.
'''

from selenium import webdriver
import time

# 다운로드 받은 크롬 물리 드라이버 가동 명령
driver = webdriver.Chrome(r'C:\Users\minho\Desktop\crawling\chromedriver_win32\chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')
time.sleep(1)

# 네이버 뉴스 진입
driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)


'''

# head_btn = f'//*[@id="lnb"]/ul/li[{num}]/a/span'

for num in range(3,9): # 헤드버튼 반복문
    head_btn = driver.find_element_by_xpath(f'//*[@id="lnb"]/ul/li[{num}]/a/span').click()
    for x in range(46,49):
      politics_btn = driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{x}]/div[1]/ul/li[1]/div[2]/a').click()
'''



for x in range(3, 9):
    news_tab = f'//*[@id="lnb"]/ul/li[{x}]/a'
    driver.find_element_by_xpath(news_tab).click()
    time.sleep(0.5)

    for n in range(1, 5):
        if x > 3:
            i = 2
        else:
            i = 1
        
        try:
            news_head = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{n}]/div[{i}]/ul/li[1]/div[2]/a'
            driver.find_element_by_xpath(news_head).click()
        except:
            news_head = f'//*[@id="main_content"]/div/div[2]/div[1]/div[{n}]/div[{i}]/ul/li[1]/div/a'
            driver.find_element_by_xpath(news_head).click()

        time.sleep(0.7)
        driver.back()
        time.sleep(0.5)













    


