import csv

with open("top_cities.csv", "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['rank','city','population'])
    writer.writerows([
        [1,'상하이',24150000],
        [2,'카리치',23500000],
        [3,'베이징',21516000],
        [4,'텐진',14722100],
        [5,'이스탄불',14160467],
    ])