import time
import sys
import os
from robobrowser import RoboBrowser

#인증 정보를 환경변수에서 추출한다.
NAVER_ID=os.environ["NAVER_ID"]
NAVER_PASSWORD=os.environ["NAVER_PASSWORD"]
print("NAVER_ID:",NAVER_ID)

#RoboBrowser객체를 생성한다.
browser=RoboBrowser(
    #Beautiful Soup에서 사용할 파서를 지정한다.
    parser="html.parser",
    #일반적인 웹 브라우저의 User-Agent(FireFox)를 사용한다.
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac macOS 10.10; rv:45.0) Gecko/20100101 Firefox/45.0"
)

def main():
    #로그인 페이지를 연다.
    print("Accessing to sign in page....", file=sys.stderr)
    browser.open("https://nid.naver.com/nidlogin.login")

    #로그인 페이지에 들어가졌는지 확인한다.
    assert "네이버 : 로그인" in browser.parsed.title.string

    #name="frmNIDLogin"이라는 입력 양식을 채운다.
    #입력 양식의 name속성은 개발자 도구로 확인할 수 있다.
    form=browser.get_form(attrs={"name":"frmNIDLogin"})

    #name="id"라는 입력 양식을 채운다.
    form["id"]=NAVER_ID
    #name="pw"라는 입력 양식을 채운다.
    form["pw"]=NAVER_PASSWORD

    #입력 양식을 전송한다.
    #로그인 때 로그인을 막는 것을 회피하고자 몇 가지 추가 정보를 전송한다.
    print("Signing in....",file=sys.stderr)
    browser.submit_form(form, headers={
        "Referer":browser.url,
        "Accep-Language":"ko,en-US;q=0.7,en;q=0.3",
    })
    #주문 이력 페이지를 연다.
    browser.open("https://order.pay.naver.com/home?tabMenu=SHOPPING&frm=s_order")

    #문제가 있을 경우 HTML소스코드를 확인할 수 있게 출력한다.
    #print(browser.parsed.prettify())

    #주문 이력 페이지가 맞는지 확인한다.
    #assert "네이버페이" in browser.parsed.title.string

    #주문 이력을 출력한다.
    print_order_history()
    print("...")
def print_order_history():
    """
    주문 이력을 출력한다.
    """
    print(".....")

    #주문 이력을 순회한다: 클래스 이름은 개발자 도구로 확인한다.
    for item in browser.select(".goods_info"):
        #주문 이력 저장 전용 dict이다.
        order={}
        #주문 이력의 내용을 추출한다.
        name_element=item.select_one(".name")
        date_element=item.select_one(".info li:nth-child(0)")
        price_element=item.select_one(".info .date")
        print("-")
        #내용이 있을 때만 저장한다.
        if name_element and date_element and price_element:
            name=name_element.get_text().strip()
            date=date_element.get_text().strip()
            price=price_element.get_text().strip()
            order[name]={
                "date":date,
                "price":price
            }
            print(order[name]["date"], "-", order[name]["price"] +"원")
if __name__=="__main__":
    main()
    print()
    print("done...")