from random import randint
from flask import Flask
from decorator import random_heading_color

app = Flask(__name__)

random = randint(0,9)

@app.route("/")
def main():
    return \
        '<h1>Guess a number between 0 and 9:</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>' 


@app.route("/<int:guess>")
@random_heading_color 
def guessed_number(guess):
    if guess > random:
        return \
            'Too high, try again!</h1>' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>' 
    elif guess < random:
        return \
            'Too low, try again!</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>' 
    else:
        return \
            'You found me!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>' 
    

if __name__ == "__main__":
    app.run(debug=True)