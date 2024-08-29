#-------------------------- ERROR HANDLING --------------------------------------#
# ## TRY
# try: 
#     file = open("file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["asdasd"])
    
# ## EXCEPT 
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} was not found.")

# ## ELSE: only if no errors
# else:
#     content = file.read()
#     print(content)

# ## FINALLY: will always happen
# finally:
#     file.close()
#     print("File was closed.")
    
#-------------------------- VALUE ERROR --------------------------------------#
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Height must be under 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

#-------------------------- INDEX ERROR --------------------------------------#
# fruits = eval(input())
# # 🚨 Do not change the code above

# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#   try:
#       fruit = fruits[index]
#   except IndexError:
#     print("Fruit pie")
#   else:
#     print(fruit + " pie")

# make_pie(4)

#-------------------------- KEY ERROR --------------------------------------#
# eval() function will create a list of dictionaries using the input
# facebook_posts = eval(input())

# total_likes = 0
# for post in facebook_posts:
#   try:
#     # TODO: Catch the KeyError exception
#     total_likes = total_likes + post['Likes']
#   except KeyError: 
#     pass
    
# print(total_likes)