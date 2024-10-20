from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from forms import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row_str = ""
        row_str = row_str + f"\n{form.cafe.data}"
        row_str = row_str + f",{form.url.data}"
        row_str = row_str + f",{form.open_time.data}"
        row_str = row_str + f",{form.close_time.data}"
        row_str = row_str + f",{form.coffee_rating.data}"
        row_str = row_str + f",{form.wifi_rating.data}"
        row_str = row_str + f",{form.power_rating.data}"

        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_file.write(row_str)
        
        ### run cafes function or just have a successful submission html page

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',') #csv.reader returns rows of data
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


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