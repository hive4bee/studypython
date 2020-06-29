import re
import pymysql
from urllib.request import urlopen
from html import unescape

def connectDB():
    mydb=pymysql.connect(
        host="localhost",
        port=3306,
        user='eprot',
        passwd='1234',
        db='mydb'
    )
    return mydb


def main():
    """
    메인 처리입니다.
    fetch(), scrape(), save() 함수를 호출한다.
    """
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)

def fetch(url):
    """
    매개변수로 전달받을 url을 기반으로 웹페이지를 추출한다.
    웹페이지의 인코딩 형식은 Content-type헤더를 기반으로 알아낸다.
    반환값: str 자료형의 html
    """
    f = urlopen(url)
    #HTTP 헤더를 기반으로 인코딩 형식을 추출한다.
    encoding=f.info().get_content_charset(failobj='utf-8')
    #추출한 인코딩 형식을 기반으로 문자열을 디코딩한다.
    html=f.read().decode(encoding)
    return html

def scrape(html):
    """
    매개변수 html로 받은 HTML을 기반으로 정규표현식을 사용해 도서 정보를 추출한다.
    반환값: 도서(dict)리스트
    """
    books=[]
    #re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출한다.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        #도서의 URL을 추출한다.
        url=re.search(r'<a href="(.*?)">', partial_html).group(1)
        url="http://www.hanbit.co.kr"+url
        #태그를 제거해서 도서의 제목을 추출한다.
        title=re.sub(r'<.*?>', '', partial_html)
        title=unescape(title)
        books.append({"url":url,"title":title})

    return books
def save(db_path, books):
    """
    매개변수 books로 전달된 도서 목록을 DB에 저장한다.
    데이터베이스의 경로는 매개변수 db_path로 지정한다.
    반환값 : NONE
    """
    #데이터베이스를 열고 연결을 확립한다.
    conn=connectDB()
    cursor=conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute(
        "CREATE TABLE books("
        "title text,"
        "url text)"
    )
    for i in range(len(books)):
        print(tuple(books[i]))
    #cursor.executemany("INSERT INTO books VALUES(:title, :url)", books)
    #conn.commit()
    #conn.close()
if __name__ == "__main__":
    main()