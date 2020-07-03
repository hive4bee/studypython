from selenium import webdriver

driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://d2.naver.com/helloworld")
print(driver.title)
driver.set_window_size(320, 600)
driver.save_screenshot("naver-responsible1.png")
driver.set_window_size(800,600)
driver.save_screenshot("naver-responseible2.png")
driver.quit()