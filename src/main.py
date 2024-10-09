import csv

filename = "../data/Emissions.csv"

def csvToDictionary(filename): 
    dataDictionary = {}
    with open(filename,'r') as file:
        csvRead = csv.reader(file)

        headers = next(csvRead)

        for row in csvRead:
            country = row[0]
            values = row[1:]
            dataDictionary[country] = values
    
    return dataDictionary, headers

def emissionYear(headers,year):
    if year in headers:
        year_index = headers.index(year) - 1
    emissions_list = {}
    for country, values in data.items():
        emissions_list[country] = values[year_index]

    #future works start here
    
    return minEmission, maxEmission, avgEmission




data = csvToDictionary(filename)

print("All data from {filename} has been read into a dictionary")

yearInput = input("Select a year to find statistics (1997-2010):")
print("In {yearInput}, countries with minimum and maximum CO2 emmission levels were [{minEmission}] and [{maxEmission}] respectively.\n Average CO2 emissions in {yearInput} were {avgEmission}")


