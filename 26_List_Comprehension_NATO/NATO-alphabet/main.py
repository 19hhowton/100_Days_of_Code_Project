import pandas as pd

CSV = r"26_List_Comprehension_NATO\NATO-alphabet\nato_phonetic_alphabet.csv"
data = pd.read_csv(CSV)
nato_df = pd.DataFrame(data)

nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
response = input("What is the word you need to covert to NATO? ")
# response = "Heather"

response_nato = [nato_dict[letter.capitalize()] for letter in response]

print(response_nato)

