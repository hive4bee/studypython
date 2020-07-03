import os
import sys
import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#인증 정보를 환경변수에서 추출한다.
NAVER_ID=os.environ["NAVER_ID"]
NAVER_PASSWORD=os.environ["NAVER_PASSWORD"]
# Chrome의 WebDriver객체를 생성한다.
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#driver.implicitly_wait(3)
def main():
    """
    메인처리
    """

    #화면 크기를 설정한다.
    #driver.set_window_size(800,600)

    #로그인하고 이동한 뒤 주문 이력을 가져온다.
    sign_in(driver)
    #navigate(driver)
    goods=scrape_history(driver)

    #출력한다.
    print(goods)

def sign_in(driver):
    """
    로그인한다.
    """
    print("Navigating....", file=sys.stderr)
    print("Waiting for sign in page loaded....",file=sys.stderr)
    time.sleep(2)
    driver.get("https://nid.naver.com/nidlogin.login")
    time.sleep(2)
    #입력 양식을 입력하고 전송한다.
    '''
    e=driver.find_element_by_id("id")
    e.clear()
    e.send_keys(NAVER_ID)
    e=driver.find_element_by_id("pw")
    e.clear()
    e.send_keys(NAVER_PASSWORD)
    form=driver.find_element_by_css_selector("input.btn_global[type=submit]")
    form.submit()
    '''
    '''
    #id
    xpath='//*[@id="id"]'
    print(NAVER_ID)
    pyperclip.copy(NAVER_ID)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element_by_name("id").click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(2)
    #pw
    xpath = '//*[@id="pw"]'
    print(NAVER_PASSWORD)
    pyperclip.copy(NAVER_PASSWORD)
    #driver.find_element_by_xpath(xpath).click()
    driver.find_element_by_name("pw").click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    '''

    driver.get("https://nid.naver.com/nidlogin.login")
    time.sleep(3)
    driver.execute_script("document.getElementById('id').value=\'"+NAVER_ID+"\'")
    time.sleep(2)
    driver.execute_script("document.getElementById('pw').value=\'"+NAVER_PASSWORD+"\'")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

def navigate(driver):
    """
    적절한 페이지로 이동한 뒤
    """
    print("Navigating....",file=sys.stderr)
    time.sleep(10)
    #driver.get("https://mail.naver.com")
    driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
    print("Wating for contents to be loaded....",file=sys.stderr)
    time.sleep(2)

    #페이지를 아래로 스크롤한다.
    #사실 현재 예제에서는 필요 없지만 활용 예를 위해 한다.
    #스크롤을 해서 데이터를 가져오는 페잊의 경우 활용할 수 있다.
    driver.execute_script("scroll(0, document.body.scrollHeight)")
    wait=WebDriverWait(driver,10)

    #[더보기]버튼을 클릭할 수 있는 상태가 될 때까지 대기하고 클릭한다.
    #두 번 클릭해서 과거의 정보까지 들고온다.
    driver.save_screenshot("note-1.png")
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_moreButton a")))
    button.click()
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#_moreButton a")))
    button.click()

    #2초 대기한다.
    print("Waiting for contents to be loaded....", file=sys.stderr)
    time.sleep(2)

def scrape_history(driver):
    """
    페이지에서 주문이력을 추출한다.
    """
    time.sleep(2)
    driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
    goods=[]
    for info in driver.find_elements_by_css_selector(".goods_item"):
        #요소를 추출한다.
        link_element=info.find_element_by_css_selector("a")
        title_element=info.find_element_by_css_select("span")
        date_element=info.find_element_by_css_select(".date")
        price_element=info.find_element_by_css_selector("em")
        #텍스트를 추출한다.
        goods.append({
            "url":link_element.get_attribute(".a"),
            "title":title_element.text,
            "description":date_element.text+" - "+price_element.text+"원"
        })
    return goods
if __name__=="__main__":
    main()

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(2)