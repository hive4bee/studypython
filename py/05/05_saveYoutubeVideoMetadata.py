import sys
from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING

#환경변수에서 API키를 추출한다.
YOUTUBE_API_KEY=""

def main():
    #MongoDB 클라이언트 객체를 생성한다.
    mongo_client=MongoClient("localhost", 27017)
    #youtube 데이터베이스의 videos 콜렉션을 추출한다.
    collection=mongo_client.youtube.videos
    #기존의 모든 문서를 제거한다.
    collection.delete_many({})

    #동영상을 검색하고, 페이지 단위로 아이템 목록을 저장한다.
    for items_per_page in search_videos("요리"):
        save_to_mongodb(collection, items_per_page)

    #뷰 수가 높은 동영상을 출력한다.
    show_top_videos(collection)

def search_videos(query, max_pages=5):
    """
    동영상을 검색하고, 페이지 단위로 list를 yield한다.
    """
    #youtube의 API 클라이언트 생성하기
    youtube=build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    #search.list 메서드로 처음 페이지 추출을 위한 요청 전소하기
    search_request=youtube.search().list(
        part="id", #search.list에서 동영상 ID만 추출해도 괜찮음
        q=query,
        type="video",
        maxResults=50, #1페이지에 최대 50개의 동영상 추출
    )
    print(search_request)
    #요청이 성공하고 페이지 수가 max_pages보다 작을 때 반복
    #페이지 수를 제한하는 것은 실행 시간이 너무 길어지는 것을 막기 위해서이다.
    #더 많은 페이지를 요청해도 상관없다.
    i=0
    while search_request and i < max_pages:
        #요청을 전송한다.
        search_response=search_request.execute()
        #동영상 ID의 리스트를 추출한다.
        video_ids = [item['id']['videoId'] for item in search_response['items']]

        #videos.list 메서드로 동영상의 상세 정보를 추출한다.
        videos_response=youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        #현재 페이지 내부의 아이템을 yield한다.
        yield videos_response['items']

        #list_next()메서드로 다음 페이지를 추출하기 위한 요청을 보낸다.
        search_request=youtube.search().list_next(search_request, search_response)
        i+=1

def save_to_mongodb(collection, items):
    """
    MongoDB에 아이템을 저장한다.
    """
    #MongoDB에 저장하기 전에 이후에 사용하기 쉽게 아이템을 가공한다.
    for item in items:
        #각 아이템의 id속성을 _id속성으로 사용한다.
        item['_id']=item['id']
        #statistics에 포함된 viewCount
        for key, value in item['statistics'].items():
            item['statistics'][key]=int(value)

    #콜렉션에 추가한다.
    result = collection.insert_many(items)
    print("Inserted {0} documents".format(len(result.inserted_ids)), file=sys.stderr)

def show_top_videos(collection):
    """
    MongoDB의 콜렉션 내부에서 뷰 수를 기준으로 상위 5개를 출력한다.
    """
    for item in collection.find().sort("statistics.viewCount",DESCENDING).limit(5):
        print(item['statistics']['viewCount'],item['snippet']['title'])

if __name__=="__main__":
    main()