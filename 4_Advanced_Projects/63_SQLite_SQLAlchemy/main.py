from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from book_form import BookForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlalchemy as sa


################################# CONFIG #################################
app = Flask(__name__)
class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
Bootstrap5(app)
db.init_app(app)


################################# TABLE SET UP #################################
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

################################# TRIAL ################################# 
# all_books = []
# # all_books = [{'title': 'Whoopty', 'author': 'ERS', 'rating': '10'}]

# # CREATE RECORD
# with app.app_context():
#     new_book = Book(title="Pandora Learns", 
#                     author="Deb Weitz", 
#                     rating=7.2)
#     db.session.add(new_book)
#     db.session.commit()

################################# ROUTING ################################# 

# @app.route('/')
# def home():
#     print(all_books)
#     return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        new_book = Book(
                    title= form.name.data, 
                    author= form.author.data, 
                    rating= form.rating.data)
        db.session.add(new_book)
        db.session.commit()   
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