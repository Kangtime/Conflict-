import json
import csv

#creating a variable that contains conflicts from Asia and Africa only in the year 2000
Asia_Africa_2000 = [] # list of lists - each element is a list for a conflict, e.g. [region1, type1]
with open ('./Individual Assignment/conflict_data/conflict_data_full_lined.json', encoding = 'utf-8-sig') as file:
    conflict = json.load(file)
    for line in conflict:
        if (line['region'] == 'Asia') and (line['year'] == 2000):
            Asia_Africa_2000.append([line['region'], line['type_of_violence']])
        if (line['region'] == 'Africa') and (line['year'] == 2000):
            Asia_Africa_2000.append([line['region'], line['type_of_violence']])
#print(Asia_Africa_2000)
#making a csv with region and type of violence
with open ('Asia_Africa_2000.csv','w') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['region', 'type_of_violence'])
    for line in Asia_Africa_2000:
        filewriter.writerow(line)
