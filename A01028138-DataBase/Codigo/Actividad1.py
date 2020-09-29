import csv
population_2010 = [ ]
co2_2010 = [ ]
value_errors = ["--", "NA"]
country_exceptions = ["World", "Country", "Asia & Oceania", "Africa", "Europe", "European Union", "Central & South America", "North America", "Eurasia", "Middle East" ]
year = ["2010"]
criteria = ["greenhouse_gas_ghgs_emissions_including_indirect_co2_without_lulucf_in_kilotonne_co2_equivalent"]

with open("populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        if row[-1] not in value_errors and row[0] not in country_exceptions:
            population_2010.append([float(row[-1]), row[0]])

population_2010.sort(reverse=True)
print(population_2010[:5])

with open("greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader = csv.reader(csvFile)

    for column in reader:
        if column[0] not in country_exceptions and column[1] in year and column[2] not in value_errors and column[3] in criteria:
            co2_2010.append([int(column[1]), float(column[2]), column[0]])

co2_2010.sort(reverse=True)
print(co2_2010[:5])

#Si, los datos se relacionan ya que los paises con mayor poblacion son los que mas gases invernaderos producen, cabe resaltar que China, India, Indonesia y Brazil no estan siendo tomados en cuenta en los datos de gases invernaderos.


