import csv

f = open('eggs.csv', 'w', newline='', encoding='utf-8')
wr = csv.writer(f)
wr.writerow([1,'john' , False])
wr.writerow([2, 'james', True])
f.close()