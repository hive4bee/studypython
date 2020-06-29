import lxml.html
#HTML파일을 읽어 들이고, getroot()메서드로 HtmlElement객체를 생성한다.
tree=lxml.html.parse("full_book_list.html")
html=tree.getroot()
#cssselect() 메서드로 a요소의 리스트를 추출하고 반복을 돌린다.
for a in html.cssselect("a"):
    #href속성과 글자를 추출한다.
    print(a.get("href"), a.text)