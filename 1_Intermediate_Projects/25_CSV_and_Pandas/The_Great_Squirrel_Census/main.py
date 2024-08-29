"""
Using the "Primary Fur Color" column, get the count of all the colors of the squirrels

- read csv as df
- what are all the different colors? .unique()
- remove nans
- data[data == 'type of color'] -> count of all colors
"""
import pandas as pd
PATH = r"25_CSV_and_Pandas\The_Great_Squirrel_Census\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pd.read_csv(PATH)
# print(squirrel_data.columns)
# 'Primary Fur Color'
primary_fur_colors = squirrel_data['Primary Fur Color']
primary_fur_colors_no_na = primary_fur_colors.dropna()

colors_list = primary_fur_colors_no_na.unique()

count_list = []
for color in colors_list:
    count_list.append(len(primary_fur_colors[primary_fur_colors == color]))
    
data_dict = {
    "Color": colors_list,
    "Count": count_list
}

df = pd.DataFrame(data_dict)
print(df)



