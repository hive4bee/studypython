'''
ls=[0,0,0,0]
sum=0
print("len(ls) :",len(ls))
for i in range(len(ls)):
    ls[i]=int(input(str(i) + "째 숫자 입력: "))
    sum+=ls[i]
for i in range(len(ls)):
    print("ls[%d]: %d"%(i, ls[i]))
print("리스트의 sum : ",sum)

print("a"+"b")
'''
#얕은 복사
ls=[10,20,30,40]
arr=ls
print("ls : ", ls, " / ls id : ", id(ls))
print("arr : ", arr, " / arr id :", id(arr))

#깊은 복사
ls=[10,20,30,40]
arr=ls[:]
arr[2]=20000
print("ls : ", ls, " / ls id : ", id(ls))
print("arr : ", arr, " / arr id :", id(arr))

ls=[10,20,30]
arr=[40,50,60]
print("ls + arr => ",ls+arr)
print("ls * 3 => ", ls*3)

#선택정렬 알고리즘
ls=[4,8,2,7,6]
print(ls)
i,j=0,0
for i in range(4):
    for j in range(i+1, 5):
        if ls[i]>ls[j]:
            ls[i],ls[j]=ls[j],ls[i]
print(ls)

#리스트 조작함수
#append(값):제일 뒤에 값추가
#pop():제일 뒤의 값을 빼고 빼낸 값삭제
#sort():항목정렬
#reverse():역순으로 정렬
#index(찾을 값):지정한 값을 찾아서 그 위치를 반환
#insert(위치,값):지정된 위치에 값을 삽입한다.
#remove(지울값):리스트에서 지정한 값을 제거, 값이 여러 개라면 첫 번째 값만 제거
#extend(리스트):리스트의 더하기 기능이다
#count(찾을 값):리스트에서 찾을 값의 개수를 센다
#len(ls):리스트에 포함된 전체 항목의 개수를 센다.

