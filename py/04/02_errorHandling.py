import time
import requests
#일시적인 오류를 나타내는 상태 코드를 지정한다.
TEMPORARY_ERROR_CODES=(408,500,502,503,504)

def main():
    """
    메인 처리
    """
    response=fetch("http://httpbin.org/status/200,404,503")
    if 200 <= response.status_code < 300:
        print("Success!!")
    else:
        print("Error!!")

def fetch(url):
    """
    지정한 url에 요청한 뒤 Response 객체를 반환한다.
    일시적인 오류가 발생하면 최대 3번 재시도한다.
    """
    max_retries=3 # 최대 3번 재시도한다.
    retries=0 #현재 재시도 횟수를 나타내는 변수이다.
    while True:
        try:
            print("Retrieving {0}....".format(url))
            response=requests.get(url)
            print("Status: {0}".format(response.status_code))
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response #일시적인 오류가 아니라면 response를 반환한다.
        except requests.exceptions.RequestException as ex:
            #네트워크 레벨 오류(RequestException)의 경우 재시도를 한다.
            print("Exception occured: {0}".format(ex))
            retries+=1
            if retries >= max_retries:
                #재시도 횟수 상환을 넘으면 예외를 발생시켜버린다.
                raise Exception("Too many retries...")
            #지수 함수적으로 재시도 간격을 증가한다.
            wait=2**(retries-1)
            print("Waiting {0} seconds....".format(wait))
            time.sleep(wait)
if __name__=="__main__":
    main()
