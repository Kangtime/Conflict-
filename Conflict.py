import json
import csv

#creating a variable that contains conflicts from Asia and Africa only in the year 2000
World_Year = []
Year_2000 = []
Asia_Africa_2000 = [] # list of lists - each element is a list for a conflict, e.g. [region1, type1]
#making a list that includes the year on top of region and type of violence, including every line of the data
with open ('conflict_data_full_lined.json', encoding = 'utf-8-sig') as file:
    conflict = json.load(file)
    for line in conflict:
        World_Year.append([line['region'], line['type_of_violence'], line['year']])
#making a list that includes all the data that shows conflicts that occured in 2000, with information on their region and type of violence
with open ('conflict_data_full_lined.json', encoding = 'utf-8-sig') as file:
    conflict = json.load(file)
    for line in conflict:
        Year_2000.append([line['region'], line['type_of_violence']])
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
with open ('World_Year.csv','w') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['region', 'type_of_violence', 'year'])
    for line in World_Year:
        filewriter.writerow(line)
with open ('2000.csv','w') as file:
    filewriter = csv.writer(file)
    filewriter.writerow(['region', 'type_of_violence', 'year'])
    for line in Year_2000:
        filewriter.writerow(line)
