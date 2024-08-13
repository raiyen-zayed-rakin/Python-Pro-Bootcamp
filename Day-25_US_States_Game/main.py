# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())
#
# print(data.condition)

# Get data in row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print(monday_temp * 9/5 + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
#
# gray = 0
# red = 0
# black = 0
# for colors in data["Primary Fur Color"]:
#     if colors == "Gray":
#         gray += 1
#     elif colors == "Cinnamon":
#         red += 1
#     else:
#         black += 1
# s_dict = {
#     "colors": ["Gray", "Red", "Black"],
#     "count": [gray, red, black]
# }
# new_data = pandas.DataFrame(s_dict)
# new_data.to_csv("s_data.csv")

gray_s_count = len(data[data["Primary Fur Color"] == "Gray"])
red_s_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [gray_s_count, red_s_count, black_s_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("New_S.csv")