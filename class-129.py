import csv 
data= []

with open ("tabularData.csv",'r') as f :
    csvReader=csv.reader(f)
    for row in csvReader:
        data.append(row)

headers=data[0]
planet_data=data[1:]
for dataPoint in planet_data:
    dataPoint[0]=dataPoint[0].lower()

#sorting data in alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[0])
with open("sortedData.csv","a+")as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)
