import csv

with open("top_cities2.csv", "w", newline="") as f:
    writer=csv.DictWriter(f,['rank','city','population'])
    writer.writerows([
        {'rank':1, 'city':'상하이','population':24150000},
        {'rank':2, 'city':'카라치', 'population':23500000}
    ])