#pip install pyquery
from pyquery import PyQuery as pq
d=pq(filename="full_book_list.html")#경로를 지정해서 파싱할 수 있다.
d=pq(url="http://example.com")#URL를 지정해서 파싱할 수도 있다.

#문자열을 지정해 파싱할 수도 있다.
d=pq('''
<html>
<head><title>온라인 과일 가게</title></head>
<body>
<h1 id="main">오늘의 과일</h1>
<ul>
    <li>사과</li>
    <li class="featured">귤</li>
    <li>포도</li>
</ul>
</body>
</html>''')

#css선택자를 지정해서 HTML객체를 추출
d('h1')
type(d('h1'))
d('h1')[0]
d('h1').text()
d('h1').attr('id')
d('h1').attr.id
d('h1').attr['id']
d('h1').parent()

d('li')
d('li.featured')
d("#main")
d("body").find("li")
d("li").filter(".featured")
d('li').eq(1)