import requests
import lxml.html

def main():
    #여러 페이지를 크롤링할 것이므로 Session을 이용한다.
    session=requests.Session()
    response=session.get("http://www.hanbit.co.kr/store/books/new_book_list.html")
    urls=scrape_list_page(response)
    for url in urls:
        #print("in main....   ",url)
        response=session.get(url)
        ebook=scrape_detail_page(response)
        print(ebook)
        #break

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect(".view_box .book_tit a"):
        url = a.get("href")
        print(url)
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출한다.
    """
    root=lxml.html.fromstring(response.content)
    ebook={
        "url":response.url,
        "title":root.cssselect(".store_product_info_box h3")[0].text_content(),
        "price":root.cssselect(".pbr strong")[0].text_content(),
        "content":[p.text_content()\
                   for p in root.cssselect("#tabs_3 .hanbit_edit_view p")]
    }
    return ebook

if __name__ == "__main__":
    main()