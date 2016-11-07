import csv

csvfile = open('zoo.data', newline='')
csvData = csv.reader(csvfile, delimiter=',', quotechar='|')

tab = []
for row in csvData:
    tab.append(row)

i = 0
dict = {}
for i in range(len(tab)):
    key = tab[i].pop(0)
    dict[key] = tab[i]


print(dict)

