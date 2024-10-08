from flask import Flask, render_template, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my secret"

@app.route("/", methods=['GET', 'POST'])
def login():
    email = None
    password = None
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" \
            and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
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