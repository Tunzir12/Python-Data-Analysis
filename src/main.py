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

filename = '../data/Emissions.csv'
data = read_csv_to_dict(filename)
print(data)