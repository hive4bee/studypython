import time
import requests
from retrying import retry # pip install retrying
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
#stop_max_attempt_number로 최대 재시도 횟수를 지정한다.
#wait_exponential_multiplier로 특정한 시간만큼 대기하고 재시도하게 한다. 단위는 밀리초로 입력한다.
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(url):
    """
    지정한 url에 요청한 뒤 Response 객체를 반환한다.
    일시적인 오류가 발생하면 최대 3번 재시도한다.
    """
    max_retries=3 # 최대 3번 재시도한다.
    retries=0 #현재 재시도 횟수를 나타내는 변수이다.
    while True:

        print("Retrieving {0}....".format(url))
        response=requests.get(url)
        print("Status: {0}".format(response.status_code))
        if response.status_code not in TEMPORARY_ERROR_CODES:
            return response #일시적인 오류가 아니라면 response를 반환한다.
        #오류가 있다면 예외를 발생시킨다.
        raise Exception("Temporary Error: {0}".format(response.status_code))
if __name__=="__main__":
    main()
