# file = open("24_Files_Directories\my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

## Read the file without using .close() method
# with open("24_Files_Directories\my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write a new line
with open("24_Files_Directories\my_file.txt", mode="w") as file:
    file.write("\nAnother line.")

## Create new file that didn't exist (must be in write mode)
# with open(r"24_Files_Directories\new_file.txt", mode="w") as file:
#     file.write("\nAnother line.")
