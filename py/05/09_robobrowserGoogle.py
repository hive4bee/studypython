#pip install robobrowser chardet
from robobrowser import RoboBrowser

#키워드 매개변수 parser는 BeautifulSoup()의 매개변수와 같다.
browser = RoboBrowser(parser="html.parser")

#open() 메서드로 구글 메인 페이지를 연다.
browser.open("https://www.google.com")

#키워드를 입력한다.
form=browser.get_form(action="/search")
form['q']="Python"
browser.submit_form(form, list(form.submit_fields.values())[0])
print(browser)
print(browser.select(".rc > a"))
#검색 결과 제목을 추출한다.
#select()메서드는 BeautifulSoup의 select()메서드와 같다.
for a in browser.select("r > a"):
    print("??")
    print(a.text)
    print(a.get("href"))
    print()