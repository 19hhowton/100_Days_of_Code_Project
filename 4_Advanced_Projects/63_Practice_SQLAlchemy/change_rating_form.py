from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length

class ChangeRatingForm(FlaskForm):
    new_rating = StringField('New Rating', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Change Rating')