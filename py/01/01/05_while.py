i=0;
while i<5:
    print(i)
    i+=1
print("next")

i=1
odd,even =0,0
while i<=10:
    if i%2==0:
        even+=i
    else:
        odd+=i
    i+=1
print("even sum : ", even)
print("odd sum : ", odd)

i=0;
while i<5:
    print(i)
    i+=1
else:
    print("조건식이 거짓일 경우 : ",i)
print("next")

i=1
flag=True
while flag:
    print("i : ", i)
    if i == 10:
        flag=False
    i+=1

num,result,i=0,0,1
while True:
    num=int(input("1~10 사이의 숫자입력:"))
    if num<1 or num>10:
        print("잘못입력")
        continue
    break
else:
    print("next")
while i<=num:
    result+=i;
    i+=1
else:
    print("1~",num,"까지의 sum : ",result)