#문자열함수
#대문자/소문자의 변환
#upper()
#lower()
#swapcase():대소문자 상호변경
#title():각 단어의 제일 앞 글자만 대문자로 변경
str="Python is Easy"
print(str)
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())
#문자열 찾기
#count(str)
#find(str)
#index(str)
#startwith(str)
#endwith(str)
str="Have a nice day"
print(str)
print()
print(str.count('a'))
print(str.count('day'))
print(str.find('kkk'))#return -1
print(str.find('day'))
#print(str.index('kkk'))#return error
print(str.index('a',2))
#문자열변경
#strip(str)
#rstrip(str)
#lstrip(str)
#replace(str1, str2)
str="  python python python   "
print(str)
print()
print(str.strip())
print(str.replace('python', 'java'))
#문자열변경
#split(str)
#splitlines()
#join(str)
str="never ever give up"
print(str)
print(str.split())
str="never\never\ngive\nup"
print(str)
print(str.splitlines())
str="%"
print(str.join('1 2 34'))

#문자열 정렬
#center(str)
#ljust(str)
#rjust(str)
#zfill(str)

#문자열 구성 파악
#isdigit()
#isalpha()
#isalnum()
#islower()
#isupper()
#isspace()