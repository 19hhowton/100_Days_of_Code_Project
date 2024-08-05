import os
import time
from tkinter import *
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"

#------------------------------ Random Word ----------------------------------#

french_words_df = pd.read_csv(r"31_Flashcard_App\data\french_words.csv")
french_dict = french_words_df.to_dict(orient="records")
print(f"the original: {len(french_dict)}")
current_card = {'French': 'matin', 'English': 'morning'}


def new_card():
    global current_card, flip_timer
    
    ## Create new french dict using the update csv
    # new_french_words = pd.read_csv(r"31_Flashcard_App\data\french_words.csv")
    new_french_dict = {}
    new_french_dict = new_french_words.to_dict(orient="records")
    
    window.after_cancel(flip_timer)
    current_card = random.choice(new_french_dict)
    print(len(french_dict))
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"])
    print(f"new_card {current_card}")
    window.after(3000, func=flip_card)
    
    

#------------------------------ Know the Card ----------------------------------#       

def knew_card():
    ## Remove from the french_word.csv
    # Remove from df
    global new_french_words
    try:
        print(f"To remove: {current_card['French']}")
        to_remove = new_french_words[new_french_words.French == current_card['French']]
        print(f"to remove: {to_remove}")
        index = to_remove.index
        print(f"index: {index}")
        new_french_words = new_french_words.drop(index)
        print(len(new_french_words))
    except:
        print(f"To remove: {current_card['French']}")
        to_remove = french_words_df[french_words_df.French == current_card['French']]
        print(f"to remove: {to_remove}")
        index = to_remove.index
        print(f"index: {index}")
        new_french_words = french_words_df.drop(index)
        print(len(new_french_words))
    finally: 
        new_french_words.to_csv(r"31_Flashcard_App\data\words_to_learn.csv")
        new_card()

    
#------------------------------ Flip Card ----------------------------------#       

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])

#------------------------------ UX ----------------------------------#
window = Tk()
window.title("French Flashcards Program")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

## Canvas
canvas = Canvas(width=800, height=526)

## Front Background Img
card_front_img = PhotoImage(file=r"31_Flashcard_App\images\card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

## Text 
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

## Back Background Img
card_back_img = PhotoImage(file=r"31_Flashcard_App\images\card_back.png")
# card_back_img = canvas.create_image(400, 263, image=back_image)
# back_button = Button(image=back_image, highlightthickness=0)

## Incorrect Button
wrong_image = PhotoImage(file=r"31_Flashcard_App\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

## Right Button
right_image = PhotoImage(file=r"31_Flashcard_App\images\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=knew_card)
right_button.grid(column=1, row=1)

window.mainloop()