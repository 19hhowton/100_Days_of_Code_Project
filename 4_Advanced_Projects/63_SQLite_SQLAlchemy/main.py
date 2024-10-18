from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from book_form import BookForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

all_books = []
# all_books = [{'title': 'Whoopty', 'author': 'ERS', 'rating': '10'}]

@app.route('/')
def home():
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        all_books.append({
                            "title": form.name.data,
                            "author": form.author.data,
                            "rating": form.rating.data,
                        })
        print(all_books)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)













'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''