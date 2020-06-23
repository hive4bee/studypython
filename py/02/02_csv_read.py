import csv

f = open('eggs.csv', 'r', encoding='utf-8')
rdr=csv.reader(f)
for line in rdr:
    print(line)
f.close()
print("//////////////////////////////////////////")
print("//////////////////////////////////////////")
with open("eggs.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for txt in reader:
        print(txt)