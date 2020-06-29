#pip install beautifulsoup4
from bs4 import BeautifulSoup #bs4 모듈에서 BeautifulSoup 클래스를 읽어 들인다.
#첫 번째 매개변수에 파일 객체를 지정해 BeautifulSoup객체를 생성한다.
#BeautifulSoup()에는 파일 이름 또는 URL을 지정할 수 없다.
#두 번째 매개변수에는 파서의 종류를 지정한다.
with open("full_book_list.html") as f:
    soup=BeautifulSoup(f, "html.parser")
#BeautifulSoup생성자에는 HTML문자열을 전달할 수도 있다.
soup=BeautifulSoup('''
<html><head><title>온라인 과일 가게</title></head>
<body>
<h1 id="main">오늘의 과일</h1>
<ul><li>사과</li><li class="featured">귤</li><li>포도</li></ul></body></html>''', 'html.parser')

soup.h1 #soup.h1처럼 태그 이름을 가진 속성으로 h1요소를 추출할 수 있다.
type(soup) #bs4.BeautifulSoup객체
type(soup.h1) #Tag객체
soup.h1.name #name속성으로 태그 이름을 추출할 수 있다.
soup.h1.string #Tag객체의 string속성으로 요소 바로 아래의 문자열을 추출할 수 있다.
type(soup.h1.string) #string속성은 str을 상속한 NavigableString객체이다.
soup.ul.text #text속성은 요소 내부의 모든 문자열을 결합해서 문자열을 추출한다.
type(soup.ul.text)#text속성은 str객체이다.
soup.h1['id'] #Tag객체는 딕셔너리처럼 속성을 추출할 수 있다.
soup.h1.get("id") #딕셔너리처럼 get()메서드로도 속성을 추출할 수 있다.
soup.h1.attrs #attr 속성으로 모든 속성을 나타내는 딕셔너리 객체를 추출할 수 있다.
soup.h1.parent #parent 속성으로 부모 요소를 추출할 수 있다.
soup.li #여러 개의 요소가 있는 경우 가장 앞의 요소를 추출하게 된다.
soup.find("li") #find()메서드도 마찬가지
soup.find_all("li") #find_all()메서드로 지정한 이름의 요소 리스트를 추출할 수 있다.
#키워드 매개변수로 class등의 속성을 지정할 수 있다. class는 예약어이므로 class_로 사용해야한다.
soup.find_all("li", class_="featured")
soup.find("li",class_="featured")
soup.find_all(id="main")
soup.find(id="main")

soup.select("li") #select()메서드로 css선택자와 일치하는 요소를 추출할 수 있다.
soup.select("li.featured")
soup.select("#main")
soup.select(".featured")

with open("full_book_list.html") as f:
    soup=BeautifulSoup(f,"html.parser")

for a in soup.find_all("a"):
    print(a.get("href"), a.text)