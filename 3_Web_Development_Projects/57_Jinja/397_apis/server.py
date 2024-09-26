from flask import Flask, render_template
from apis import get_gender, get_age

app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)