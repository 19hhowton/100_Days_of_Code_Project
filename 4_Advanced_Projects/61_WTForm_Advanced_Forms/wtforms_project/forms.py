from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[InputRequired(), Email()])
    password = PasswordField("Password: ", validators=[InputRequired(), Length(min=8)])
    submit = SubmitField("Submit")