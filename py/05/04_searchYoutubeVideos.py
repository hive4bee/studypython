#pip install google-api-python-client
from apiclient.discovery import build

YOUTUBE_API_KEY=""

#Youtube API 클라이언트를 생성한다.
#build() 함수의 첫 번째 매개변수에는 API이름
#두 번째 매개변수에는 API버전을 지정
#키워드 매개변수 developerKey에는 API 키를 지정한다.
#이 함수는 내부적으로 https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest라는
#URL에 접근하고 API리소스와 메서드 정보를 추출한다.
youtube=build("youtube","v3",developerKey=YOUTUBE_API_KEY)

#키워드 매개변수로 매개변수를 지정하고
#search.list 메서드를 호출한다.
#list() 메서드를 실행하면 googleapiclient.http.HttpRequest가 반환된다.
#execute()메서드를 실행하면 실제 HTTP 요청이 보내지며, API응답이 반환된다.
search_response=youtube.search().list(
    part="snippet",
    q="요리",
    type="video",
    maxResults="10"
).execute()

#search_response는 API응답을 JSON으로 나타낸 dict객체이다.
for item in search_response['items']:
    #동영상 제목을 출력한다.
    print(item["snippet"]["title"])