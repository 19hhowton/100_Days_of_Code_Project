from tkinter import *
from tkinter import messagebox
import random
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list 

    random.shuffle(password_list)

    password = "".join(char for char in password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def data_entry():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()
    
    ## Raise warning for empty entry fields
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Small Mistake", message="You have at least one empty entry.")
        
    else:  
        ## MessageBox
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details" 
                                f"entered: \nEmail: {email} \nPassword: {password}"
                                f"\nIs it ok to save?")
        
        ## Store the Entries
        if is_ok:
            data = r"29_Password_Manager_Project\data.txt"
            with open(data, "a") as f:
                combined = f"{email} | {website} | {password} \n"
                f.write(combined)
        
            ## Clear the Entry fields
            email_input.delete(0, END)
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

## Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=r"29_Password_Manager_Project\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

## Website Text
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

## Email/Username Text
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

## Password Text
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

## Website Entry
website_input = Entry(width=43)
website_input.grid(column=1, row=1, columnspan=2)
website_input.insert(0, "www.amazon.com/in")

## Email/Username Entry
email_input = Entry(width=43)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "19hhowton@gmail.com")

## Password Entry
password_input = Entry(width=25)
password_input.grid(column=1, row=3, columnspan=1)
password_input.insert(0, "SDFA120!")

## Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

## Add Button
add_button = Button(text="Add", width=36, command=data_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()