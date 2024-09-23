from flask import Flask
from challenge_386.decorator import make_bold, make_emphasis, make_underlined

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)