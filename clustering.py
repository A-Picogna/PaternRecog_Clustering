import csv

csvFile = None;

csvfile = open('zoo.data', newline='')
csvData = csv.reader(csvfile, delimiter=',', quotechar='|')

tab = []
for row in csvData:
    tab.append(row)

i = 0
newTab = {}
for i in range(len(tab)):
    key = tab[i].pop(0)
    newTab[key] = tab[i]


print(newTab)

