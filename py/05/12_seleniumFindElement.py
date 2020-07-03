from selenium import webdriver
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://www.hanbit.co.kr/store/books/look.php?p_code=B8967937297")

#find_elements_by_css_selector는 . 또는 # 을 명시해 줘야한다.
#반면, find_elements_by_class_name, find_elements_by_id는 그렇지 않아도 된다.
print(driver.find_elements_by_css_selector(".store_product_info_box"))
print(driver.find_elements_by_css_selector(".store_product_info_box")[0])
#하나의 DOM 요소는 webElement객체에 대응한다.
#div=driver.find_element_by_css_selector(".store_product_info_box")[0]
div=driver.find_elements_by_class_name("store_product_info_box")[0]
#속성을 추출할 때는 get_attribute()메서드를 사용한다.
div.get_attribute("class")

#요소 내부에서 요소를 추가로 탐색할 수도 있다.
h3=div.find_elements_by_css_selector("h3")[0]
print(h3)
#내부의 글자를 추출할 때는 text속성을 사용한다.
print(h3.text)

driver.quit()