from pymongo import MongoClient
#호스트 이름과 포트번호를 지정해서 접속한다.
#localhost와 27017은 기본값이므로 생략해도 상관없다
client=MongoClient("localhost", 27017)
#test디비를 추출한다. 디비가 존재하지 않으면 자동으로 생성한다.
db = client.test
db = client['test'] #딕셔너리처럼도 사용할 수도 있다.
#디비의 spots콜렉션을 추출한다. 콜렉션이 존재하지 않으면 자동으로 생성한다.
collection = db.spots
collection = db['spots']

#insert_one() 메서드로 딕셔너리를 콜렉션에 삽입한다.
collection.insert_one({"name":"N서울타워","prefecture":"서울"})

#insert_many() 메서드로 여러 개의 딕셔너리를 컬렉션에 삽입한다.
collection.insert_many([{"name":"첨성대","prefecture":"경주"},{"name":"롯데월드타워","prefecture":"서울"}])

#find() 메서드를 사용해 문서를 추출하는 Cursor객체를 추출한다.
#모든 문서에는 _id필드가 자동으로 붙으며, 해당 값은 ObjectId라고 하는 12바이트 식별자이다.
collection.find()
#Cursor객체는 for구문으로 반복할 수 있다.
for spot in collection.find():
    print(spot)
#find()메서드의 매개변수로 쿼리를 지정하면
#해당 쿼리에 맞는 문서가 추출된다.
#다음 쿼리는 prefecture필드가 '서울'인 문서를 추출한다.
for spot in collection.find({"prefecture":"서울"}):
    print(spot)

client.close()