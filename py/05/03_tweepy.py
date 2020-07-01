import tweepy

#환경변수에서 인증 정보를 추출한다.
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

#인증정보를 설정한다.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#API클라이언트를 생성한다.
api = tweepy.API(auth)

keyword="주가"#검새하고 싶은 키워드 입력
result=[]#크롤링 텍스트를 저장할 리스트 선언

for i in range(1,3):#page1~2
    tweets=api.search(keyword)
    for tweet in tweets:
        result.append(tweet)

print(len(result))
print(result)
