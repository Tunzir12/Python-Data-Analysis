import csv

def read_csv_to_dict(filename):
    data_dict = {}
    with open(filename, 'r') as csvfile:
        reader =  csv.reader(csvfile)
        next(reader)
        for row in reader:
            country = row[0]
            data_list = [float(value) for value in row[1:]]
            data_dict[country] = data_list
    return data_dict

def analyze_emissions(data_dict):
    year = int(input("Select a year to find statistics(1997 to 2010): "))
    year_index = year - 1997
    emissions_in_year = [data_dict[country][year_index] for country in data_dict]

    min_emission = min (emissions_in_year)
    max_emission = max (emissions_in_year)
    avg_emission = sum (emissions_in_year) / len(emissions_in_year)

    min_country = [country for country in data_dict if data_dict[country][year_index] == min_emission]
    max_country = [country for country in data_dict if data_dict[country][year_index] == max_emission]

    print(f"In {year}, countries with minimum and maximum CO2 emission level were: {min_country} and {max_country} respectively.")
    print(f"Average CO2 emissions in {year} were {avg_emission:.6f}")

filename = '../data/Emissions.csv'
data = read_csv_to_dict(filename)
analyze_emissions(data)