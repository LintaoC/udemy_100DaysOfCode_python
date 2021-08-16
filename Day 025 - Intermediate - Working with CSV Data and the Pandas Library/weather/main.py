# with open("weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(row[1])
#
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))  # Panda DataFrame (2D Data)
print(type(data["temp"]))  # Panda Series (1D Data)

data_dict = data.to_dict()  # Pandas DataFrame (2D Data) can be converted to Dict
print(data_dict)

data_list = data["temp"].to_list()  # Pandas Series (1D Data) can be converted to list
print(data_list)

# Get Data in Columns
print(data["condition"])  # Columns can be selected with key argument (kind of like a Dict)...
print(data.condition)  # But columns can also be selected directly with .column_name (kind of like an object)

# Get Data in rows
print(data[data["day"] == "Monday"])

average_temp = data["temp"].mean()  # Pandas can do various calculation on a series, like mean, max, sum,...
print(average_temp)

max_temp = data["temp"].max()  # Pandas can do various calculation on a series, like mean, max, sum,...
print(max_temp)

# Example to return the row with the maximum temperature
max_temp = data["temp"].max()
print(data[data["temp"] == max_temp])
monday = data[data["day"] == "Monday"]
# Example calculate a var from a row
monday_temp_celcius = int(monday["temp"])
monday_temp_fahrenheit = monday_temp_celcius * 1.8 + 32
print(monday_temp_celcius)
print(monday_temp_fahrenheit)

# Create a dataframe from Scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_from_dict = pandas.DataFrame(data_dict)  # Create the DataFrame
data_from_dict.to_csv("students_data.csv")  # Save the DataFrame into a new file
