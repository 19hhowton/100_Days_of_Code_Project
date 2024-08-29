PATH = "25_CSV_and_Pandas\weather_data.csv"

# with open(PATH) as file:
#     weather_list = file.readlines()

# cleaned_weather_list = []
# for row in weather_list:
#     x = row.strip("\n")
#     cleaned_weather_list.append(x)
    
# print(weather_list)
# print(cleaned_weather_list)


# """List of temperature data, stored as intergers."""
# import csv

# temperature_list = []
# counter = 0
# with open(PATH) as file:
#     data = csv.reader(file)
#     for row in data:
#         counter += 1
#         if counter == 1:
#             pass
#         else:
#             temperature_list.append(int(row[1]))
# print(temperature_list)

import pandas

data = pandas.read_csv(PATH)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

### Get data in Column
# print(data["temp"])
# print(data.temp)

### Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

### Get the series of data but convert to fereneight 
# F=(9/5)C+32
# x = (data.temp * (9/5)) + 32
# print(x)

### Create a dataframe from scratch
# data_dict = {
#     "students": ["Heather", "Sharada", "Anu"],
#     "scores": [93, 95, 99]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

