import csv

filename = "../data/Emissions.csv"

# Function to read the CSV and store data in a dictionary
def csvToDictionary(filename):
    dataDictionary = {}
    with open(filename, 'r') as file:
        csvRead = csv.reader(file)
        headers = next(csvRead)  # Read the header row

        for row in csvRead:
            country = row[0]  # Country is the first column
            values = row[1:]  # Emission data are the rest of the columns
            dataDictionary[country] = values

    return dataDictionary, headers

# Function to calculate statistics (min, max, avg) for the given year
def emissionYear(headers, year, data):
    if year in headers:
        year_index = headers.index(year)  # Get the correct year index from headers
        emissions_list = []

        for country, values in data.items():
            emissions_value = values[year_index]  # Retrieve emission value for the specific year
            try:
                emissions_list.append(float(emissions_value))  # Convert to float and add to the list
            except ValueError:
                continue  # Skip if there's an invalid value (e.g., missing data)

        if emissions_list:  # Check if we have valid emission data
            minEmission = min(emissions_list)  # Minimum value
            maxEmission = max(emissions_list)  # Maximum value
            avgEmission = sum(emissions_list) / len(emissions_list)  # Average value
            return minEmission, maxEmission, avgEmission
        else:
            return None, None, None  # No valid data for the year
    else:
        return None, None, None  # Year not found in the headers

# Main execution of the script
data, headers = csvToDictionary(filename)

print(f"All data from {filename} has been read into a dictionary.")

# Input year from user
yearInput = input("Select a year to find statistics (1997-2010): ")
minEmission, maxEmission, avgEmission = emissionYear(headers, yearInput, data)

# Output the results
if minEmission is not None and maxEmission is not None and avgEmission is not None:
    print(f"In {yearInput}, the minimum CO2 emission was {minEmission:}, "
          f"the maximum was {maxEmission}, and the average was {avgEmission}.")
else:
    print(f"Invalid year or no valid data available for the year {yearInput}.")
