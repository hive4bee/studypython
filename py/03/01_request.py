import requests
r=requests.get("http://hanbit.co.kr")#웹 페이지 추출
print(type(r))#response자료형
print(r.status_code) #status_code속성으로 http 상태코드를 확인
print(r.headers['content-type']) #headers속성으로 http헤더를 딕셔너리로 추출
print(r.encoding)
print(r.text) #text속성으로 str자료형으로 디코딩된 응답 본문을 추출
print(r.content)
print(r.json)
r=requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010")
print(r.json)
r=requests.post("http://httpbin.org/post",data={"key1":"value1"})
#키워드 매개변수 data에 딕셔너리를 지정하면 html 입력 양식처럼 전송된다.

#이 밖에도 요청에 추가할 http헤더, auth인증키워드 등을 지정한다.
r=requests.get("http://httpbin.org/get",headers={"user-agent":"my-crawler/1.0 (+foo@example.com)"})
r=requests.get("https://api.github.com/user",auth=("<GitHub의 사용자 ID>","<GitHub의 비밀번호>"))
r=requests.get("http://httpbin.org/get",param={"key1":"value1"})#URL매개변수는 키워드 매개변수 param으로도 지정가능

#Session객체를 사용해 같은 웹사이트에 여러 번 요청할 때는 http keep-alive라는 접속방식이 사용된다
#한 번 확립한 tcp 요청을 계속 활용하므로 오버헤드가 되는 TCP커넥션 확립처리를 줄일 수 있어서 성능향상을 기대할 수 있다
#특히 https로 시작되는 url에 요청을 보낼 때는 tcp 네트워크 확립에 암호화를 위한 TLS/SSL 핸드셰이크를
#하게되는데, 부하가 꽤나 많이 걸리는 처리이다. 게다가 http keep-alive를 사용하면
#서버 측 부하도 줄일 수 있다.

#http헤더를 여러 번 사용할 때는 session객체를 사용한다.
s=requests.Session()
s.headers.update({"user-agent":"my-crawler/1.0 (+foo@example.com)"})

#session객체에는 get(), post() 등의 메서드가 있다.
#requests.get(), requests.post() 등과 같은 방식으로 사용한다.
r=s.get("http://naver.com")
r=s.get("http://daum.net")
