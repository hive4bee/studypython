import re
res = re.match("You", "Young Frankenstein")
print("res : " , res)

youpattern=re.compile("You")
res2 = youpattern.match("Young Frankenstein")
print("res2 :",res2)

source="Young Frankenstein Frank"
m = re.search("Frank", source)
print("m :",m)
if m:
    print("m.group() :",m.group())

print("re.findall() :",re.findall("e.?n", source))
m=re.findall("n.?", source)
print("m :",m)

cp = re.compile("n.?")
print("result : ", re.findall(cp, source))

str="eeprot@naver.com"
cp2 = re.compile("(.*)@")
cp3 = re.compile("@(.*)")
print("cp2 result :", re.findall(cp2, str))
print("cp3 result :", re.findall(cp3, str))