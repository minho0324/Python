


# 셀레늄 : 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium(셀레늄 라이브러리 다운로드)
# 셀레늄 임포트
from selenium import webdriver
import time

# 다운로드 받은 크롬 물리 드라이버 가동 명령
driver = webdriver.Chrome(r'C:\Users\minho\Desktop\crawling\chromedriver_win32\chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')
time.sleep(1)

'''
# 자동으로 버튼이나 링크 클릭 제어하기.
login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn.click()

time.sleep(1.5)

# 자동으로 아이디 입력하기
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('minho0324')

time.sleep(1)

# 자동으로 비번 입력하기
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('abc1234')

time.sleep(1)

# 로그인버튼 클릭
driver.find_element_by_xpath('//*[@id="log.login"]').click()
'''



# 네이버에 접속해서 검색창에 '오늘 날씨'를 입력해서
# 검색 후 가장 첫번쨰로 뜨는 네이버 뉴스를 띄워주세요

# 검색창에 '오늘 날씨' 타이핑
search_btn = driver.find_element_by_xpath('//*[@id="query"]')
# search_btn = driver.find_element_by_xpath('//*[@id="query"]').send_keys('오늘 날씨')
search_btn.send_keys('오늘 날씨')

time.sleep(1)

# 엔터
search_input = driver.find_element_by_xpath('//*[@id="search_btn"]')
# search_input = driver.find_element_by_xpath('//*[@id="search_btn"]').click()
search_input.click()

time.sleep(1)

# 해당 기사 클릭
news_btn = driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/div[1]/div/a')
# news_btn = driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/div[1]/div/a').click()
news_btn.click()



