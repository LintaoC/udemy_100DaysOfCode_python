import pandas

#FUR_COLORS = ["Gray", "Cinnamon", "Black"]

# Read the data from the CSV
data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Convert data to a list
list_primary_fur_color = data_squirrel["Primary Fur Color"].to_list()

# # NOTE: I can retrieve all row with "Gray" in it with the below code
# grey_fur_raw_list = data_squirrel[data_squirrel["Primary Fur Color"] == "Gray"]
# I can then count with  len() to get the number of "Gray" squirrel
# print(grey_fur_raw_list)

# Count the number of grey, black and cinnamon fur on the list, using pandas .count() method
grey_fur = list_primary_fur_color.count("Gray")
black_fur = list_primary_fur_color.count("Black")
cinnamon_fur = list_primary_fur_color.count("Cinnamon")
print(grey_fur, black_fur, cinnamon_fur)

# Convert the fur colors into a Dict
fur_color_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_fur, cinnamon_fur, black_fur]
}
fur_color_dataframe = pandas.DataFrame(fur_color_data)  # Create the DataFrame
fur_color_dataframe.to_csv("squirrel_count.csv")  # Save the DataFrame into a new file