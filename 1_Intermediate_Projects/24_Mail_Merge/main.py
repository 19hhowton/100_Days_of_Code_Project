#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r"24_Mail_Merge\Input\Names\invited_names.txt", "r") as file:
    invited_names = file.readlines()

cleaned_invited_names = []
for name in invited_names:
    name = name.strip('\n')
    cleaned_invited_names.append(name)
print(cleaned_invited_names)

with open('24_Mail_Merge\Input\Letters\starting_letter.txt') as file:
    content = file.read()
    for name in cleaned_invited_names:
        with open(f"24_Mail_Merge\Output\ReadyToSend\{name}.txt", "w") as f:
            content_with_name = content.replace("[name]", f"{name}")
            f.write(content_with_name)
            