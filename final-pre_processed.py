import csv

dataSet1=[]
dataSet2=[]

with open ("final-webScraping.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet1.append(row)

headers1=dataSet1[0]
planet_data1=dataSet1[1:]

with open ("sortedData.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet2.append(row)

headers2=dataSet2[0]
planet_data2=dataSet2[1:]

headers=headers1+headers2
planet_data=[]

for index, dataRow in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("finalData.csv","a+")as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)