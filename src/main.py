import csv

filename = "../data/Emissions.csv"

def csvToDictionary(filename): 
    dataDictionary = {}
    with open(filename,'r') as file:
        csvRead = csv.reader(file)

        for row in csvRead:
            country = row[0]
            values = row[1:]
            dataDictionary[country] = values
    
    return dataDictionary


data = csvToDictionary(filename)

for key, value in data.items():
    print(f'{key}:{value}')
