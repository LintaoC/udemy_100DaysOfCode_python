# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (value,key) in dict.items()}
# new_dict = {new_key:new_value for (value,key) in dict.items() if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Angela"]

import pandas
student_dict = {
    "Student" : ["Angela", "James", "Lily"],
    "Score" : [56, 61, 99]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    #print(row)
    print(row["Student"])
    print(row["Score"])
    print(row["Student"][0])