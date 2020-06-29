'''
for i in range(0, 3, 1):
    print("i : %d"%i, "for문 이해하기")
print("다음 문장들 실행")
'''

'''
for i in range(1, 11, 1):
    if i % 2 == 0:
        print("i=%d"%i, "->짝수")
    else:
        print("i=%d"%i, "->홀수")
print("다음 문장")
'''


for i in range(1,31,1):
    if i % 5 == 0:
        print("%d"%i)
    else:
        print(i,end="\t")


for i in [1,2,3,4,5,6,7,8,9,10]:
    print("i : %d"%i)

st = "Hello Python"
for c in st:
    print("c : %c"%c)

list=[10, "test", 123.123]
print("list :",list)
print()
for i in list:
    print(i)