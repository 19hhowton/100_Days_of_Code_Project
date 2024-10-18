from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), Length(max=20)])
    author = StringField('Book Author', validators=[DataRequired(), Length(max=20)])
    rating = StringField('Rating', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Submit')