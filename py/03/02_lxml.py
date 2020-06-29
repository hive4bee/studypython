#sudo apt-get install -y libxml2-dev libxslt-dev libpython3-dev zlib1g-dev
#pip install lxml
#pip install cssselect
#wget http://www.hanbit.co.kr/store/books/full_book_list.html
import lxml.html
tree = lxml.html.parse("full_book_list.html") #parse()함수로 파일경로를 지정할 수 있다.
#parse()함수로 URL을 지정할수도 있지만 추출할 때 미세한 설정을 따로 할 수 없으므로 추천하지 않는다.
tree=lxml.html.parse("http://example.com")
#파일 객체를 지정해서 파싱할 수도 있다.
from urllib.request import urlopen
tree=lxml.html.parse(urlopen("http://example.com/"))
type(tree)#파싱하면 ElementTree 객체가 추출된다
html=tree.getroot()#getroot() 메서드로 html루트 요소의 HtmlElement 객체를 추출할 수 있다.
type(html)

#fromstring()함수로 문자열(str 자료형 또는 byte 자료형)을 파싱할 수 있다.
#참고로 encoding이 지정된 xml선언을 포함한 str을 파싱하면 ValueError가 발생하므로 주의해야한다.
html=lxml.html.fromstring('''
<html>
<head><title>온라인 과일 가게</title></head>
<body>
<h1 id="main">오늘의 과일</h1>
<ul>
    <li>사과</li>
    <li class="featured">귤</li>
    <li>포도</li>
</ul></body></html''')
type(html)
html.xpath("//li") #XPath와 일치하는 요소 목록을 추출할 수 있다.
html.cssselect("li") #선택자와 일치하는 요소목록을 추출할 수 있다.
h1=html.xpath("//h1")[0]
h1.tag #tag속성으로 태그의 이름을 추출할 수 있다.
h1.text #text속성으로 요소의 텍스트를 추출할 수 있다.
h1.get("id") #get() 메서드로 속성 값을 추출할 수 있다.
h1.attrib #attrib속성으로 모든 속성을 나타내는 딕셔너리 같은 객체를 추출할 수 있다.
h1.getparent() #getparent()메서드로 부모 요소를 추출할 수 있다.

