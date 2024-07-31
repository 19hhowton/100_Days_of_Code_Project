# new_list = [i*2 for i in list (if ...)]
import random

numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

### Moving through list and creating a dictionary
# names_list = ["Alex", "John", "Sara", "Caroline", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1, 100) for student in names_list}
# print(students_scores)

### Moving through dictionary and creating a dictionary
"""new_dict = {new_key:new_value for (key, value) in dict.items() if test}"""
# = or over 60 . 
# students_scores = {name:grade for (name, grade) in students_scores.items() if grade >= 60}
# print(students_scores)

### Moving through pandas dataframe creating a ...
"""for (index, row_data) in student_df.iterrows(): 
    print(row_data.column_name)"""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}