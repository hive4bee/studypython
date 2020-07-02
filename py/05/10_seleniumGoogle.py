#pip install selenium==3.0
#wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
#tar xvf phantomjs-1.9.8-linux-x86_64.tar.bz2
#cp phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin
#apt-get install -y fonts-nanum*
#phantomjs --version
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

#PhantomJS 모듈의 WebDriver 객체를 생성한다.
#driver=webdriver.PhantomJS("/usr/local/bin/phantomjs")
driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(3)
#Google메인 페이지를 연다.
driver.get("https://www.google.co.kr")

#타이틀에 "google"이 포함되어 있는지 확인한다.
#assert "Google" in driver.title

#검색어를 입력하고 검색한다.
input_element=driver.find_element_by_name("q")
input_element.clear()
input_element.send_keys("Python")
input_element.send_keys(Keys.RETURN)

#타이틀에 "Python"이 포함돼 있는지 확인한다.
assert "Python" in driver.title

#스크린샷을 찍는다.
driver.save_screenshot("search_results.png")

for a in driver.find_elements_by_css_selector("h3 > a"):
    print(a.text)
    print(a.get_attribute("href"))
    print()