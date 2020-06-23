student={'학번':1234,'이름':'홍길동','학과':'it학과'}
print(student)
mobile={"품명":"겔럭시","가격":100,"크기":10}
print(mobile)

impo={}
impo['python']='www.python.org'
impo['naver']='www.naver.com'
impo['google']='www.google.com'
print(impo)

#딕셔너리함수
#keys():key list
#values():value list
#items():key, value list
#clear():clear all
#get(key):if exist then print value, or none
#setdefault(key,value):키가 없으면 추가설정
#updata(ojb):다른 사전의 내용으로 갱신
#popitem():(key,value)를 리턴하고 항목제거
#fromkeys(key) or fromkeys(key,value) : 리스트나 튜플로 설정
#pop(key):key를 이용하여 해당하는 값을 지움
print(impo.keys())
print(impo.values())
print(list(impo))
