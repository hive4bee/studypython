import lxml.html
from pymongo import MongoClient

#HTML 파일을 읽어 들이고
#getroot()메서드를 사용해 HtmlElement객체를 추출한다.
tree=lxml.html.parse("full_book_list.html")
html=tree.getroot()

client=MongoClient("localhost", 27017)
db=client.scraping #scraping 데이터베이스를 추출한다.
collection=db.links #links 콜렉션을 추출

#스크립트를 여러 번 사용해도 같은 결과를 출력할 수 있게 컬렉션의 문서를 제거한다.
collection.delete_many({})

#cssselect() 메서드로 a요소의 목록을 추출한다.
for a in html.cssselect('a'):
    #href 속성과 링크의 글자를 추출해서 저장한다.
    collection.insert_one({
        "url":a.get("href"),
        "title":a.text
    })