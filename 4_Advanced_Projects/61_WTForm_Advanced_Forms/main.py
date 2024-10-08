from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my secret"


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[InputRequired(), Email()])
    password = PasswordField("Password: ", validators=[InputRequired(), Length(min=8)])
    submit = SubmitField("Submit")

@app.route("/", methods=['GET', 'POST'])
def login():
    email = None
    password = None
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template("login.html", login_form = login_form)

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
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