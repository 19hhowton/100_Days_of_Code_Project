from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from book_form import BookForm
from change_rating_form import ChangeRatingForm

app = Flask(__name__)

# BOOTSTRAP CONFIG
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


# DATABASE CONFIG
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# TABLE CONFIG
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


# ROUTING
@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_rating(id):
    change_rating_form = ChangeRatingForm()
    if request.method == "POST":
        book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()  
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("edit_rating.html", book_id=id, books=all_books, form=change_rating_form)

@app.route("/delete/<id>")
def delete(id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)