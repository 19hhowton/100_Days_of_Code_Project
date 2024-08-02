import pandas as pd

CSV = r"26_List_Comprehension_NATO\NATO-alphabet\nato_phonetic_alphabet.csv"
data = pd.read_csv(CSV)
nato_df = pd.DataFrame(data)

nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

response = "Heather"

is_on = True
while is_on:
    response = input("What is the word you need to covert to NATO? ")
    response_nato = []
    try: 
        for letter in response:
            response_nato.append(nato_dict[letter.capitalize()])
    except KeyError:
        print("Sorry, only letters in the alphabet are supported.")        
    else:
        print(response_nato)
        is_on = False
        

# response_nato = [nato_dict[letter.capitalize()] for letter in response]
# print(response_nato)


