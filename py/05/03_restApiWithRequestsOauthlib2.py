import os
#pip install tweepy
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
#사용자의 타임라인을 추출한다.
public_tweets=api.home_timeline()

for status in public_tweets:
    #사용자 이름과 트윗을 출력한다.
    print("@" + status.user.screen_name, status.text)