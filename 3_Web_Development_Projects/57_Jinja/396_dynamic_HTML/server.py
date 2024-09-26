from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def home():
    curr_year = datetime.today().year
    # random_number = random.randint(1, 10)
    return render_template("index.html", curr_year=curr_year)

if __name__ == "__main__":
    app.run(debug=True)