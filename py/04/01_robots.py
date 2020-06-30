import urllib.robotparser
rp=urllib.robotparser.RobotFileParser()

#set_url()로 robots.txt의 URL을 설정한다.
rp.set_url("http://wikibook.co.kr/robots.txt")

#read()로 robots.txt를 읽어 들인다.
rp.read()

#can_fetch()의 첫 번째 매개변수에는 User-Agent문자열,
#두 번째 매개변수에 URL을 지정하면 해당 URL을 크롤링해도 괜찮은지 알 수 있다.
rp.can_fetch("mybot", "http://wikibook.co.kr")
